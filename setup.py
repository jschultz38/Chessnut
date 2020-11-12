#How to send that bitch over to pip: https://dzone.com/articles/executable-package-pip-install

from setuptools import setup
import os

long_description = 'A simple chess model in pure Python'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

# https://pythonhosted.org/setuptools/setuptools.html#id7
setup(
    name='Chessnut4jschultz38',
    version='0.3.10',
    packages=['Chessnut'],
    author="Jarrett S",
    author_email="jschultz38@gatech.edu",
    description="A basic chess model to imports/export FEN & finds moves. Made to fix an issue with parent repo.",
    long_description=long_description,
    license="UNLICENSE",
    keywords="chess",
    url="https://github.com/jschultz38/Chessnut",
)
