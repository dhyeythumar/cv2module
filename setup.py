import os
from setuptools import setup

BASE_DEPENDENCIES = [
    'opencv-python>=4.2.0.32',
    'numpy>=1.18.1',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

# # allow setup.py to be run from any path
# BASEDIR = os.path.dirname(os.path.abspath(__file__))
# os.chdir(os.path.normpath(BASEDIR))

setup(
    name="cv2module",
    packages=["cv2module"],
    version="0.1",
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dhyey Thumar",
    author_email="dhyeythumar@gmail.com",
    description="A package that provides various functions to assist the OpenCV workflow",
    url="https://github.com/Dhyeythumar/cv2module",
    install_requires=BASE_DEPENDENCIES,
    keywords=['cv2', 'color', 'mask'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
