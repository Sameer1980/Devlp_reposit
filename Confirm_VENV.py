/*How to know I'm using venv Python
Jul 26, 2023

Several ways to know if the Python interpreter is running inside a virtual environment:

Solution 1: use sys.prefix that points to the Python directory
Solution 2 (the better way): VIRTUAL_ENV environment variable. When a virtual environment is activated, this is set to the venv’s directory, 
otherwise it’s None.*/

print (sys.prefix)
import os
print (os.environ.get('VIRTUAL_ENV'))