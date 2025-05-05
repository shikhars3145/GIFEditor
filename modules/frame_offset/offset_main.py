from PIL import Image
import os
import json

def offset_frames(file_path, output_folder, offset_percentage):
    """Offset each frame of a GIF by a given percentage of the width, wrapping from right to left."""
    try:
        with Image.open(file_path) as img:
            frame_number = 0
            offset_pixels = int((offset_percentage / 100) * img.width)

            durations = []

            while True:
                # Create a new image with the same size as the original
                offset_frame = Image.new("RGBA", img.size)

                # Paste the original image twice to handle wrapping
                offset_frame.paste(img, (-offset_pixels, 0))
                offset_frame.paste(img, (img.width - offset_pixels, 0))

                # Save the offset frame
                frame_path = os.path.join(output_folder, f"offset_frame_{frame_number}.png")
                offset_frame.save(frame_path)

                # Append the duration of the current frame
                durations.append(img.info.get('duration', 100))

                frame_number += 1
                try:
                    img.seek(frame_number)
                except EOFError:
                    break

            # Save updated durations
            updated_durations_file = os.path.join(output_folder, "durations.json")
            with open(updated_durations_file, "w") as f:
                json.dump(durations, f)

        print(f"Offset frames and durations saved to {output_folder}")
    except Exception as e:
        print(f"Error: {e}")