 ## Building the App like a PyPi Package

from setuptools import find_packages,setup
from typing import List


EDITABLE_FLAG = '-e .' 

def get_requirements(file_path:str)->List[str]: # arrow fn 
    """
    this function will a List of requirements ,as a list of strings
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace("\n", "")  for req in requirements] # list comprenhension ,to edit list
        
        if EDITABLE_FLAG in requirements:
            requirements.remove(EDITABLE_FLAG)

    return requirements


setup(
    name='First End to End',
    version = '0.0.1',
    author='hemang',
    packages=find_packages(),
    # install_requires=['pandas','numpy','seaborn']
    install_requires = get_requirements('requirements.txt')
    
    
)