### import the url library


import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)


##### modular_example/arithmetic

### SEE ARITHMETIC AND CALCULATIONS FILES


def add(x,y):
    return x + y
def multiply(x,y):
    return x*y
def subtract(x,y):
    return x-y







from my_package.subdirectory import my_functions

#### example
sample_project
     |_____ python_file.py
     |_____ my_modules
               |_____ __init__.py
               |_____ test_module.py
               |_____ another_module.py
               |_____ third_module.py



###### both these requests get the same thing

import my_modules.test_module

from my_modules import test_module

