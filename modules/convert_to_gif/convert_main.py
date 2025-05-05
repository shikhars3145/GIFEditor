from PIL import Image
import os
import re
import json
from modules.utils.common import numerical_sort

def convert_frames_to_gif(input_folder, output_file):
    """Convert frames in a folder into a single GIF."""
    try:
        frames = []

        # Clear the output file if it already exists
        if os.path.exists(output_file):
            os.remove(output_file)

        for file_name in sorted(os.listdir(input_folder), key=numerical_sort):
            file_path = os.path.join(input_folder, file_name)
            if os.path.isfile(file_path) and file_name.endswith(('.png', '.jpg', '.jpeg')):
                frames.append(Image.open(file_path))

        if frames:
            # Load frame durations
            durations_file = os.path.join(input_folder, "durations.json")
            with open(durations_file, "r") as f:
                durations = json.load(f)

            # Save the frames as a new GIF with durations
            frames[0].save(output_file, save_all=True, append_images=frames[1:], loop=0, duration=durations)
            print(f"GIF created at {output_file}")
        else:
            print("No valid image frames found in the input folder.")
    except Exception as e:
        print(f"Error: {e}")