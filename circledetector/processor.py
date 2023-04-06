import os
import cv2
import numpy as np
import pydicom
import csv


class CircleDetector:
    """
    A class that detects circles in DICOM images and saves the circle information in a CSV file.
    """

    def __init__(self, dp=1, minDist=50, param1=50, param2=30, minRadius=10, maxRadius=50):
        """
        Initializes a CircleDetector object with Hough transform parameters.

        Args:
            dp (float): Inverse ratio of the accumulator resolution to the image resolution (default: 1).
            minDist (float): Minimum distance between the centers of the detected circles (default: 50).
            param1 (int): First method-specific parameter (default: 50).
            param2 (int): Second method-specific parameter (default: 30).
            minRadius (int): Minimum radius of the detected circles (default: 10).
            maxRadius (int): Maximum radius of the detected circles (default: 50).
        """
        self.dp = dp
        self.minDist = minDist
        self.param1 = param1
        self.param2 = param2
        self.minRadius = minRadius
        self.maxRadius = maxRadius

    def load_dicom_image(self, file_path):
        """
        Loads a DICOM image from a file path.

        Args:
            file_path (str): The file path of the DICOM image.

        Returns:
            numpy.ndarray: The loaded DICOM image as a numpy array.
        """
        ds = pydicom.dcmread(file_path)
        img = ds.pixel_array.astype(np.float32)
        img = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)
        img = img.astype(np.uint8)
        return img

    def detect_circles(self, img):
        """
        Detects circles in a given image using the Hough transform.

        Args:
            img : The image to detect circles in.

        Returns:
            An array of circles in the format (x, y, r).
        """
        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=self.dp, minDist=self.minDist,
                                   param1=self.param1, param2=self.param2, minRadius=self.minRadius, maxRadius=self.maxRadius)
        if circles is None:
            return None
        circles = np.round(circles[0, :]).astype("int")
        return circles

    def save_circle_info(self, circles, output_file):
        """
        Saves circle information to a CSV file.

        Args:
            circles (numpy.ndarray): An array of circles in the format (x, y, r).
            output_file (str): The output CSV file path.
        """
        with open(output_file, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['x position', 'y position', 'radius'])
            for (x, y, r) in circles:
                writer.writerow([x, y, r])

    def detect_and_save_circles(self, file_path, output_file):
        """
        Detects circles in a DICOM image and saves the circle information to a CSV file.

        Args:
            file_path (str): The file path of the DICOM image.
            output_file (str): The output CSV file path.
        """
        img = self.load_dicom_image(file_path)
        circles = self.detect_circles(img)
        if circles is not None:
            self.save_circle_info(circles, output_file)
