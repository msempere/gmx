import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "gmx",
    version = "0.0.1",
    author = "msempere",
    author_email = "msempere@gmx.com",
    description = ("An interface for GMX Mail."),
    license = "MIT",
    keywords = "gmx email",
    url = "https://github.com/msempere/gmx",
    packages=['gmx'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Communications :: Email",
        "License :: OSI Approved :: MIT License",
    ],
)
