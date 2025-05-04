# Product Requirements Document (PRD)

## Overview
This project is a Python-based GIF editor that provides the following functionalities:

1. **Preview a GIF**: Display a given GIF file for preview.
2. **Extract Frames**: Extract individual frames from a GIF file.
3. **Offset Frames**: Offset each frame by a given pixel value, wrapping the image from right to left.
4. **Increase Frames**: Extend the number of frames in a GIF by repeating the initial frames.
5. **Set Frame Timing**: Specify the time interval between different frames in a GIF.

## Goals
- Use Python libraries or free online APIs to implement the features.
- Ensure the code is modular and extendable for future enhancements.
- Use a virtual environment (venv) for package management.
- Track progress and maintain a clear development plan.

## Non-Goals
- Advanced image editing features beyond the specified requirements.

## Assumptions
- Users will provide valid GIF files as input.
- The application will run on Windows OS.

## Deliverables
- A Python program with the specified functionalities.
- A requirements file for package installation.
- A Git repository with feature-based commits.

## Updated Requirements

6. **Convert Frames to GIF**:
   - Combine individual frames from a folder (e.g., `inputs/frames_gifname`) into a single GIF file.
   - Save the resulting GIF in the `results/combinedFrames` folder with the name `gifname.gif`.

---