# GIF Editor

## Overview
This project is a Python-based GIF editor that provides various functionalities, including previewing GIFs, extracting frames, and more.

## Features
- **Preview a GIF**: Display a given GIF file for preview.
- **Extract Frames**: Extract individual frames from a GIF file and save them as images.
- **Convert Frames to GIF**: Combine individual frames from a folder into a single GIF file.

## How to Use the Preview Feature

1. Place the GIF file you want to preview in the `inputs` folder.
2. Run the following command in your terminal:

   ```bash
   python gifEditor.py preview inputs/<your_gif_file_name>.gif
   ```

   Replace `<your_gif_file_name>` with the name of your GIF file.

3. The GIF will be displayed using your default image viewer.

## How to Use the Extract Frames Feature

1. Place the GIF file you want to extract frames from in the `inputs` folder.
2. Run the following command in your terminal:

   ```bash
   python gifEditor.py extract_frames inputs/<your_gif_file_name>.gif
   ```

   Replace `<your_gif_file_name>` with the name of your GIF file.

3. The frames will be saved in the `results/<your_gif_file_name>` folder.

## How to Use the Convert Frames to GIF Feature

1. Place the frames you want to combine into a GIF in a folder named `inputs/frames_<gifname>`.
2. Run the following command in your terminal:

   ```bash
   python gifEditor.py convert_to_gif inputs/frames_<gifname>
   ```

   Replace `<gifname>` with the desired name for your GIF.

3. The resulting GIF will be saved in the `results/combinedFrames/<gifname>.gif` file.

## Example

If you have a file named `example.gif` in the `inputs` folder, use the following command:

```bash
python gifEditor.py preview inputs/example.gif
```

This will open and display the `example.gif` file.