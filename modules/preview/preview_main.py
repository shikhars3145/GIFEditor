from PIL import Image
import webbrowser
import os

def preview_gif(file_path):
    """Preview a GIF file by opening it in the default web browser."""
    try:
        abs_path = os.path.abspath(file_path)
        webbrowser.open(f"file://{abs_path}")
    except Exception as e:
        print(f"Error: {e}")