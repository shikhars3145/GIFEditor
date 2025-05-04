import sys
import os
from modules.preview.preview_main import preview_gif
from modules.extract_frames.extract_main import extract_frames

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
    else:
        print(f"Feature '{feature}' is not supported.")

if __name__ == "__main__":
    main()