'''import sys
import platform
print (sys.version)
platform.python_version()
print ('Hello world!!')'''

print (dir())
print (f'The __name__ from Basic.py is "{__name__}"')

# Python dir() function example
class Student():
    def __init__(self,x):
        return self.x
# calling function
att = dir(Student)
# Displaying result
print(att)