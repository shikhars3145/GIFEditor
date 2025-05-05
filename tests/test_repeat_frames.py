import os
import unittest
from PIL import Image
from modules.frame_repetition.repeat_main import repeat_frames

class TestRepeatFrames(unittest.TestCase):

    def setUp(self):
        self.input_gif = "inputs/bongocat.gif"
        self.output_folder = "results/test_repeated_bongocat"
        self.limit = 30  # Set the limit for the total number of frames
        os.makedirs(self.output_folder, exist_ok=True)

    def test_repeat_frames(self):
        # Run the repeat_frames function
        repeat_frames(self.input_gif, self.output_folder, self.limit)

        # Verify
        output_gif = os.path.join(self.output_folder, f"repeated_{os.path.basename(self.input_gif)}")
        with Image.open(output_gif) as img:
            frame_count = 0
            while True:
                try:
                    img.seek(frame_count)
                    frame_count += 1
                except EOFError:
                    break

        # Expected frame count = limit
        self.assertEqual(frame_count, self.limit, f"Expected {self.limit} frames, but got {frame_count}")

if __name__ == "__main__":
    unittest.main()