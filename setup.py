import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cv2.utils-dhyeythumar",  # Replace with your own username
    version="0.0.1",
    author="Dhyey Thumar",
    author_email="dhyeythumar@gmail.com",
    description="A package that provides various functions to assist the OpenCV workflow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Dhyeythumar/cv2.utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
    ],
    python_requires='>=3.6',
)
