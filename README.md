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

## How to Use the Frame Offset Feature

1. Place the GIF file you want to offset in the `inputs` folder.
2. Run the following command in your terminal:

   ```bash
   python gifEditor.py offset_frames inputs/<your_gif_file_name>.gif <offset_percentage>
   ```

   Replace `<your_gif_file_name>` with the name of your GIF file and `<offset_percentage>` with the percentage of the width by which you want to offset the frames.

3. The offset frames will be saved in the `results/offset_<your_gif_file_name>` folder.

## How to Use the Frame Repetition Feature

1. Place the GIF file you want to repeat frames for in the `inputs` folder.
2. Run the following command in your terminal:

   ```bash
   python gifEditor.py repeat_frames inputs/<your_gif_file_name>.gif <limit>
   ```

   Replace `<your_gif_file_name>` with the name of your GIF file and `<limit>` with the maximum number of frames you want in the resulting GIF.

3. The repeated GIF will be saved in the `results/repeated_<your_gif_file_name>` folder.

## Workflow for GIF Editing

1. **Remove Duplicates**:
   - Run the following command to remove duplicate frames from a GIF while preserving the total duration:

     ```bash
     python gifEditor.py remove_duplicates inputs/<your_gif_file_name>.gif
     ```

     The resulting GIF will be saved in the `results/unique_<your_gif_file_name>.gif` folder.

2. **Convert to Frames**:
   - Extract frames from the resulting GIF and save their durations:

     ```bash
     python gifEditor.py extract_frames results/unique_<your_gif_file_name>.gif
     ```

     Frames and their durations will be saved in the `results/unique_<your_gif_file_name>` folder.

3. **Repeat Frames**:
   - Repeat frames up to a specified limit:

     ```bash
     python gifEditor.py repeat_frames results/unique_<your_gif_file_name>.gif <limit>
     ```

     The repeated frames and updated durations will be saved in the `results/repeated_<your_gif_file_name>` folder.

4. **Convert Frames to GIF**:
   - Combine the repeated frames into a single GIF:

     ```bash
     python gifEditor.py convert_to_gif results/repeated_<your_gif_file_name>/repeated_frames
     ```

     The final GIF will be saved in the `results/repeated_<your_gif_file_name>` folder.

## Running Tests

To run all tests, execute the following command in your terminal:

```bash
python -m unittest discover -s tests -p "test_*.py"
```

This will discover and run all test files in the `tests` directory that match the pattern `test_*.py`.

## Running Individual Tests

To run a specific test file, use the following command:

```bash
python tests/<test_file_name>.py
```

Replace `<test_file_name>` with the name of the test file you want to run. For example, to run the test for the `repeat_frames` feature, use:

```bash
python tests/test_repeat_frames.py
```

## Example

If you have a file named `example.gif` in the `inputs` folder, use the following command:

```bash
python gifEditor.py preview inputs/example.gif
```

This will open and display the `example.gif` file.