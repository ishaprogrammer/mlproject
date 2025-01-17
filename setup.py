from setuptools import find_packages, setup
from typing import List

hypen_e_dot = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements = [requires.replace("\n","") for requires in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

setup(name="mlproject",
      version="0.0.1",
      author="Taskin Shaikh",
      author_email="ishashaikh154@gmail.com",
      packages=find_packages(),
      install_requires = get_requirements("requirements.txt") )