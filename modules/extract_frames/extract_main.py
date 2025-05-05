from PIL import Image
import os
import json

def extract_frames(file_path, output_folder):
    """Extract frames from a GIF and save them as individual images."""
    try:
        with Image.open(file_path) as img:
            frame_number = 0
            durations = []
            while True:
                frame_path = os.path.join(output_folder, f"frame_{frame_number}.png")
                img.save(frame_path)
                durations.append(img.info['duration'])
                frame_number += 1
                try:
                    img.seek(frame_number)
                except EOFError:
                    break

            # Save frame duration information
            durations_file = os.path.join(output_folder, "durations.json")
            with open(durations_file, "w") as f:
                json.dump(durations, f)

            print(f"Frames and durations saved to {output_folder}")
    except Exception as e:
        print(f"Error: {e}")