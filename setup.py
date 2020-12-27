"""Setup script for animalsay"""

import os.path
from setuptools import setup, find_packages 

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fh:
    long_description = fh.read()

# This call to setup() does all the work
setup(
    name="animalsay", # what you pip install not necesarily what you import
    version="1.0.5",
    description="A Python version of the famous cowsay program by Tony Monroe.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Gloria Macia",
    author_email="gloria.macia@roche.com",
    url="https://github.com/gloriamacia/animalsay",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.6',
    packages=find_packages() # https://stackoverflow.com/questions/43253701/python-packaging-subdirectories-not-installed
)