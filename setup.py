from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()


VERSION = '1.0.0'
DESCRIPTION = 'A utility for saving and loading data using pickle with logging functionality.'

setup(
    name="PickleHandler",
    version=VERSION,
    author="PRBN",
    author_email="<career.prabin@gmail.com>",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[pickle, os, logging],
    keywords=['python', 'pickle', 'save', 'load', 'logging'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution-ShareAlike 4.0 International License",
        "Operating System :: OS Independent",
    ]
)

