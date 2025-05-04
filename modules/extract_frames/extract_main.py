from PIL import Image
import os

def extract_frames(file_path, output_folder):
    """Extract frames from a GIF and save them as individual images."""
    try:
        with Image.open(file_path) as img:
            frame_number = 0
            while True:
                frame_path = os.path.join(output_folder, f"frame_{frame_number}.png")
                img.save(frame_path)
                frame_number += 1
                try:
                    img.seek(frame_number)
                except EOFError:
                    break
        print(f"Frames extracted to {output_folder}")
    except Exception as e:
        print(f"Error: {e}")