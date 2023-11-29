"""setup file"""

from setuptools import find_packages, setup

setup(
    name="postools",
    version="23.10.29",
    packages=find_packages(exclude=("tests", "docs")),
    description="Example python code to work within IDEAS",
    url="https://github.com/inscopix/ideas-example-tool",
    author="Srinivas Gorur-Shandilya",
    author_email="srinivas@inscopix.com",
    install_requires=[
        "matplotlib>=3.3",
        "numpy",
    ],
)
