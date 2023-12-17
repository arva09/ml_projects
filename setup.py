#create ml project as a package
from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirements
    '''
#below code is (In summary, the code is necessary to read the contents of the file specified by file_path and store them in a list (requirements). 
#This list can then be used for further processing, such as parsing and extracting information from the file, 
#especially when dealing with files that contain lists of requirements, configuration settings, or other structured data.)
  
    requirements=[]
    with open(file_path) as file_obj:# This line opens the file specified by the file_path variable.
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
 
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="ml_projects",
    version="0.0.1",
    author="arva09",
    author_email="arpitahiregoudar09@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)