"""Setup script for animalsay"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="animalsay", # what you pip install not necesarily what you import
    version="1.0.0",
    description="A Python version of the famous cowsay program by Tony Monroe",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gloria Macia",
    author_email="gloria.macia@.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    packages=["animalsay"], # what users import 
)