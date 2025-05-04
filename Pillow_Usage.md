# Pillow Library Overview and Usage Plan

## What is Pillow?
Pillow is a Python Imaging Library (PIL) fork that provides extensive support for opening, manipulating, and saving many different image file formats. It is widely used for image processing tasks such as resizing, cropping, filtering, and working with animated GIFs.

## How We Plan to Use Pillow

1. **Preview a GIF**:
   - Use Pillow's `Image` module to open and display GIF files.
   - Utilize the `Image.show()` method to preview the GIF.

2. **Extract Frames**:
   - Use the `Image.seek()` method to navigate through individual frames of a GIF.
   - Save each frame as a separate image file if needed.

3. **Offset Frames**:
   - Manipulate each frame using Pillow's image transformation methods (e.g., `Image.transform()` or `Image.paste()`) to apply pixel offsets and wrap the image from right to left.

4. **Increase Frames**:
   - Duplicate frames by copying and appending them to the sequence of frames.
   - Use Pillow's `Image.save()` method to create a new GIF with the extended frame sequence.

5. **Set Frame Timing**:
   - Modify the `duration` parameter when saving a GIF to specify the time interval between frames.

## Why Pillow?
- Pillow is a well-documented and actively maintained library.
- It supports animated GIFs and provides tools for frame-level manipulation.
- It is lightweight and easy to integrate into Python projects.

---