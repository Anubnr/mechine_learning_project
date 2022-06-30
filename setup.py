from setuptools import find_packages, setup
from typing import List
# declaring variables for setup
PROJECT_NAME = "housing-prediction"
VERSION = "0.0.1"
AUTHOR = "Anusha Kethanaboina"
DESCRIPTION = "This is my first FSDS project"
PACKAGES = ["housing"]
REQUIREMENT_FILE_NAME = "requirements.txt"



def get_requirements_list() -> List[str] :
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e")

        """Description: This function is going to return the list of requirements mentioned in the requirements.txt

returns: This function is going to return a list which contains name of libraries mentioned in the requirmnents.txt file
"""


setup(
    name = PROJECT_NAME,
    version = VERSION,
    author = AUTHOR,
    description = DESCRIPTION,
    packages = find_packages(),
    install_requires= get_requirements_list()
)



   