import os
import unittest
from processor import CircleDetector


class TestCircleDetector(unittest.TestCase):
    def test_detect_and_save_circles(self):
        detector = CircleDetector()
        file_path = "MR000000.dcm"
        output_file = "test_output.csv"
        detector.detect_and_save_circles(file_path, output_file)
        self.assertTrue(os.path.exists(output_file))


if __name__ == '__main__':
    unittest.main()
