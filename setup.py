# Responsible for creating ML project as a package and even deploy in PyPI 
# also contains metadata and instructions for building the package,

from setuptools import setup,find_packages
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(filepath:str)->list[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(filepath) as file_obj:
        reqirements=file_obj.readlines()
        reqirements=[ req.replace ("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)



setup(
name='mlproject',
version='0.0.1',
author="MITHUN",
author_email="shettigarmithun841@gmail.com",
packages=find_packages(),
# install_requires=['pandas', 'numpy', 'seaborn']
install_requires=get_requirements('requirements.txt')


)







