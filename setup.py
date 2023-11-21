from setuptools import find_packages,setup
import logging

with open('README.md',"r") as f:
    long_description = f.read()

__version__ = '0.0.0'
AUTHOR_USER_NAME = 'VishalChandru'
AUTHOR_EMAIL = 'vishalchandru3004@gmail.com'
SRC_REPO = 'Kidney_CTScan'
DEST_REPO = 'KidneyCNN'

setup(
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    name=SRC_REPO,
    version=__version__,
    description='An app to perform CNN on kidney CNN',
    long_description=long_description,
    url=f'https://github/{AUTHOR_USER_NAME}/{DEST_REPO}',
    package_dir={"":"src"},
    packages=find_packages()
)