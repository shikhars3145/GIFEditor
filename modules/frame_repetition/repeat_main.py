from PIL import Image
import os
from modules.convert_to_gif.convert_main import convert_frames_to_gif
from modules.extract_frames.extract_main import extract_frames

def repeat_frames(file_path, output_folder, repeat_count):
    """Repeat frames of a GIF a specified number of times and save the result."""
    try:
        # Extract frames from the input GIF
        temp_frames_folder = os.path.join(output_folder, "temp_frames")
        os.makedirs(temp_frames_folder, exist_ok=True)
        extract_frames(file_path, temp_frames_folder)

        # Copy frames and rename them to generate repeated frames up to the limit
        total_frames = 0
        repeated_folder = os.path.join(output_folder, "repeated_frames")
        os.makedirs(repeated_folder, exist_ok=True)

        while total_frames < repeat_count:
            for frame_file in sorted(os.listdir(temp_frames_folder)):
                if total_frames >= repeat_count:
                    break
                src_frame_path = os.path.join(temp_frames_folder, frame_file)
                dest_frame_path = os.path.join(repeated_folder, f"frame_{total_frames}.png")
                Image.open(src_frame_path).save(dest_frame_path)
                total_frames += 1

        # Use the convert_frames_to_gif function to create the GIF
        output_gif = os.path.join(output_folder, f"repeated_{os.path.basename(file_path)}")
        convert_frames_to_gif(repeated_folder, output_gif)

        print(f"Repeated GIF saved to {output_gif}")
    except Exception as e:
        print(f"Error: {e}")