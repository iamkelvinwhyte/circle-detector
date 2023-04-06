from setuptools import setup, find_packages
from circledetector import __version__

setup(
    name='circle-detector',
    version=__version__,
    description='A tool for detecting circles in DICOM images',
    author='Kelvin Odafe ',
    author_email='odafeky@gmail.com',
    packages=find_packages(exclude=["tests","*.tests","*tests.*"]),
    install_requires=[
        'numpy',
        'matplotlib',
        'pydicom',
        'opencv-python-headless',
        'pillow',
        'tk',
    ],
    entry_points={
        'console_scripts': [
            'circle-detector=circledetector.__main__:CircleDetectorGUI',
        ],
    },
    python_requires=">=3.7"
)
