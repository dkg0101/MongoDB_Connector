from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

__version__ = "0.0.2"
REPO_NAME = "MongoDB_Connector"
PKG_NAME= "mongodb_connect"
AUTHOR_USER_NAME = "dkg0101"
AUTHOR_EMAIL = "dkgurav999@gmail.com"
HYPEN_E_DOT = '-e .'

def get_requirements(filepath:str):
    requirements= []
    with open(filepath) as file:
        requirements = file.readlines()
        requirements = [req.replace('\n','') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires = get_requirements('./requirements_dev.txt')
    )