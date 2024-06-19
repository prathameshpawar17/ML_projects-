from setuptools import find_packages,setup
from typing import List
#-e , is automiculy trigar the  the rewuiremt file i dont need her 
HYPEN_E_DOT='-e .'
'''
    this function will return the list of requirements
'''
#read requirement file
# when ever the some next line is come  is come in requirements file the replace with the blank space
def get_requirements(file_path:str)->List[str]:

    requirements=[]
    with open(file_path) as file_obj:

        requirements=file_obj.readlines()

        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Prathamesh',
author_email='prathameshpawar1702@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)