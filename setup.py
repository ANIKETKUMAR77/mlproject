from setuptools import find_packages, setup
from typing import List

def get_requirements(file):
    with open(file) as f:
        reqs = [x.strip() for x in f.readlines() if x.strip()]
    return reqs

setup(
    name="mlproject",
    version="0.0.1",
    author="Aniket",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
