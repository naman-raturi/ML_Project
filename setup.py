from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from the given file.
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()  # Fixed the missing parentheses
        requirements = [req.replace("\n"," ") for req in requirements]  # Remove newline characters

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)  # Remove '-e .' if present

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="naman",
    author_email="namanraturi107@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")  # Fixed this line
)
