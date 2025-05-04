import sys
from modules.preview.preview_main import preview_gif

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
    else:
        print(f"Feature '{feature}' is not supported.")

if __name__ == "__main__":
    main()