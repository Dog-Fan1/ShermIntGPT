import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ShermintGPT",
    version = "0.0.1",
    author = "HJD and LDD",
    author_email = "henrydeller11934@gmail.com",
    description = ("An ollama-based library of AIs that you can install, remove, and chat with"),
    license = "BSD",
    keywords = "AI",
    url = "http://packages.python.org/shermintgpt",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

