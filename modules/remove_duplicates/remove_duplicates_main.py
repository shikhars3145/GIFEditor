from PIL import Image, ImageChops
import os

def remove_duplicate_frames(file_path, output_file):
    """Remove duplicate frames from a GIF while preserving total duration."""
    try:
        with Image.open(file_path) as img:
            unique_frames = []
            durations = []

            # Iterate through frames
            prev_frame = None
            while True:
                current_frame = img.copy()
                # Ensure frames have the same mode and size for comparison
                current_frame = current_frame.convert("RGBA")
                if prev_frame is not None:
                    prev_frame = prev_frame.convert("RGBA")
                    current_frame = current_frame.resize(prev_frame.size)

                if prev_frame is None or not ImageChops.difference(prev_frame, current_frame).getbbox():
                    # If the frame is unique or the first frame
                    unique_frames.append(current_frame)
                    durations.append(img.info.get('duration', 100))
                else:
                    # If the frame is a duplicate, add its duration to the last unique frame
                    durations[-1] += img.info.get('duration', 100)

                prev_frame = current_frame
                try:
                    img.seek(img.tell() + 1)
                except EOFError:
                    break

            # Save the unique frames as a new GIF
            unique_frames[0].save(output_file, save_all=True, append_images=unique_frames[1:], loop=0, duration=durations)

            print(f"Unique GIF saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")