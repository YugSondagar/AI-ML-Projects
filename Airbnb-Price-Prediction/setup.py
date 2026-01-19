from setuptools import setup,find_packages
from typing import List
import os

HYPEN_E_DOT = '-e .'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name = "Airbnb Price Prediction",
    version= "0.0.1",
    author="Yug Sondagar",
    install_requires = get_requirements(
    os.path.join(BASE_DIR, "requirements.txt")),
    packages = find_packages()
)