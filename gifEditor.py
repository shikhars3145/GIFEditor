import sys
import os
from modules.preview.preview_main import preview_gif
from modules.extract_frames.extract_main import extract_frames
from modules.convert_to_gif.convert_main import convert_frames_to_gif
from modules.frame_offset.offset_main import offset_frames
from modules.frame_repetition.repeat_main import repeat_frames
from modules.remove_duplicates.remove_duplicates_main import remove_duplicate_frames

def main():
    if len(sys.argv) < 3:
        print("Usage: python gifEditor.py <feature> <args>")
        return

    feature = sys.argv[1].lower()

    if feature == "preview":
        if len(sys.argv) != 3:
            print("Usage: python gifEditor.py preview <path_to_gif>")
        else:
            preview_gif(sys.argv[2])
    elif feature == "extract_frames":
        if len(sys.argv) != 3:
            print("Usage: python gifEditor.py extract_frames <path_to_gif>")
        else:
            gif_name = os.path.splitext(os.path.basename(sys.argv[2]))[0]
            output_folder = os.path.join("results", gif_name)
            if os.path.exists(output_folder):
                for file in os.listdir(output_folder):
                    file_path = os.path.join(output_folder, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
            else:
                os.makedirs(output_folder, exist_ok=True)
            extract_frames(sys.argv[2], output_folder)
    elif feature == "convert_to_gif":
        if len(sys.argv) != 3:
            print("Usage: python gifEditor.py convert_to_gif <frames_folder>")
        else:
            frames_folder = sys.argv[2]
            gif_name = os.path.basename(frames_folder).replace("frames_", "")
            output_file = os.path.join("results", "combinedFrames", f"{gif_name}.gif")
            os.makedirs(os.path.dirname(output_file), exist_ok=True)
            convert_frames_to_gif(frames_folder, output_file)
    elif feature == "offset_frames":
        if len(sys.argv) != 4:
            print("Usage: python gifEditor.py offset_frames <path_to_gif> <offset_value>")
        else:
            gif_name = os.path.splitext(os.path.basename(sys.argv[2]))[0]
            output_folder = os.path.join("results", f"offset_{gif_name}")
            os.makedirs(output_folder, exist_ok=True)
            offset_percentage = float(sys.argv[3])
            offset_frames(sys.argv[2], output_folder, offset_percentage)
            output_gif = os.path.join("results", f"offset_{gif_name}.gif")
            convert_frames_to_gif(output_folder, output_gif)
    elif feature == "repeat_frames":
        if len(sys.argv) != 4:
            print("Usage: python gifEditor.py repeat_frames <path_to_gif> <repeat_count>")
        else:
            gif_name = os.path.splitext(os.path.basename(sys.argv[2]))[0]
            output_folder = os.path.join("results", f"repeated_{gif_name}")
            os.makedirs(output_folder, exist_ok=True)
            repeat_count = int(sys.argv[3])
            repeat_frames(sys.argv[2], output_folder, repeat_count)
    elif feature == "remove_duplicates":
        if len(sys.argv) != 3:
            print("Usage: python gifEditor.py remove_duplicates <path_to_gif>")
        else:
            gif_name = os.path.splitext(os.path.basename(sys.argv[2]))[0]
            output_file = os.path.join("results", f"unique_{gif_name}.gif")
            remove_duplicate_frames(sys.argv[2], output_file)
    else:
        print(f"Feature '{feature}' is not supported.")

if __name__ == "__main__":
    main()