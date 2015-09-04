

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "PyAnno",
    version = "0.1a",
    author = "Julia Gustavsen",
    author_email = "jag@gmail.com",
    description = "Pyanno annotating things and labelling things.",
    license = "BSD",
    keywords = "labels voting annotation",
    url = "https://github.com/jooolia/pyanno_voting",
    packages=['pyanno'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

