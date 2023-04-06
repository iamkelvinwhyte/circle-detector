import tkinter as tk
from tkinter import filedialog
from circledetector.processor import CircleDetector
import os


class CircleDetectorGUI:
    """
    A class that implements a GUI for detecting circles in DICOM images 
    and saving the circle information in a  CSV file.
    """

    def __init__(self):
        """
        Initializes a CircleDetectorGUI object with a CircleDetector object and a Tkinter window.
        """
        self.detector = CircleDetector()

        self.root = tk.Tk()
        self.root.title("Circle Detector")
        self.root.geometry("600x450")

        self.button = tk.Button(
            self.root, text="Select DICOM Image", command=self.upload_image)
        self.button.pack(pady=10)

        self.root.mainloop()

    def upload_image(self):
        """
        Opens a file dialog to select a DICOM image and save the CSV file.
        """
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("DICOM Files", "*.dcm")])
            if file_path:
                output_file = filedialog.asksaveasfilename(
                    defaultextension=".csv", initialfile="output.csv")
                if not output_file:
                    raise Exception("No file name specified!")
                self.detector.detect_and_save_circles(file_path, output_file)
        except Exception as e:
            tk.messagebox.showerror("Error", str(e))



