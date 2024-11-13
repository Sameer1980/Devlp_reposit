# mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
# mydict={}
# for i in mylist:
#     if i not in mydict:
#       mydict[i]=1
#     else:
#         mydict[i]=mydict.get(i) + 1
# print (mydict)

# count_dict=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     if name not in count_dict:
#         count_dict[name]=1
#     else:
#         count_dict[name]=count_dict.get(name) + 1
# print (count_dict)


from collections import Counter
# mylist=[1,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3]
# print (Counter(mylist))
#
# mylist=['a','a',10,10,10]
# print (Counter(mylist))
#
# names=['csev','cwen','csev','zqian','cwen']
# print (Counter(names))

# sentence="How many times does each word show up in this sentence with a word"
# print (Counter(sentence.lower().split()))

# letters='aaaaaaaabbcccccddeeeeeeeeee'
# c=Counter(letters)
# print (type(c))
# print(c)
#
# print (c.most_common(2))
#
# print (list(c))
#=========================================================================================
from collections import defaultdict
#d={'a':10}
# print (d)
#
# print (d['a'])

# Gives error because there is no key 'WRONG'
# d['WRONG']
# print (d)

# Sets a default value even if there is no key.
# d=defaultdict(lambda : 0)
# d['CORRECT']
#print (d)

#d['WRONG']
#print (d)
#=====================================================================================
# A namedtuple is a data type in the collections module.
# It is a tuple subclass that allows you to create immutable objects with named fields.
# This improves code readability by providing meaningful names for each element and
# making the code more explicit.

from collections import namedtuple
# Dog=namedtuple('Dog',['age','breed','name'])
# sammy=Dog(age=5, breed='Husky', name='Sam')
# print (type(sammy))
# print (sammy)
# print (sammy.age)
# print (sammy[0])
#
# print (sammy.breed)
# print (sammy[1])

# SHUTIL AND OS MODULE.
# f=open('practice.txt','w+')
# f.write('This is a text string')
# f.close()

#import os

#print (os.getcwd())
#print (os.listdir())
#print (os.listdir('C:\\Users'))

import shutil
#shutil.move('practice.txt','C:\\Users')

import send2trash
#print (os.getcwd())
#print (os.listdir())
#print (shutil.move('C:\\Users\\practice.txt',os.getcwd()))
# send2trash.send2trash('practice.txt')
# print (os.listdir())

# os.walk-> It yields a tuple that contains directory path, directories name and file name.

# file_path='C:\\Project_2024\\Top_level'
#
# for folder, sub_folder, files in os.walk(file_path):
#  print (f"Currently looking at {folder}")
#  print ('\n')
#  print ('The subfolders are: ')
#  for sub_fold in sub_folder:
#         print (f"Subfolder: {sub_fold}")
#  print ('\n')
#  print ("the files are:")
#  for f in files:
#      print (f"File:{f}")
#  print ('\n')

#================================================================================
#Datetime module

import datetime
# mytime=datetime.time(15,30)
# print(type(mytime))
# print (mytime)
# #
# print (mytime.minute)
# #
# print (mytime.hour)
# #
# today=datetime.date.today()
# print (today)
# print (today.year)
# print (today.month)
# print (today.day)
# print (today.ctime())

#Python time module functions
#Python time.time()
# Epoch= The beginning of time is measured from 1 January, 12:00 a.m., 1970,
# and this time is referred to as the “epoch” in Python.
#It should be noted that this module has limits; for example,
# the functions may not handle dates and times before to the epoch or in the remote future.

#The time() method in Python returns the current time. It returns the number of seconds
# that have passed since the epoch. Assume we want to find out what time it is right now.
# We could achieve that by using the following program:

import time

# seconds = time.time()
# print('Seconds since epoch =', seconds)

#Most humans are unable to read epoch time. The Python ctime() method can be used to convert
# time from epoch to local time. The ctime() function takes a single argument.
# The time.ctime() function takes an argument of seconds since the epoch and returns
# a string representing local time.

# print (today.ctime())
# local_time=time.ctime(seconds)
# print ("Local time:",local_time )

#Python time.sleep()
#This is a pretty intriguing time module function. The  time.sleep() suspends a program’s execution
# for a specified number of seconds.
# The sleep() function suspends (delays) the current thread’s execution
# for the specified amount of seconds. The time.sleep() function accepts floating-point (decimal)
# or integer (whole) number values. If we want to print the sentences after a few seconds,
# we can do so using the following method:


# import time
#
# print('This is printed immediately')
#
# time.sleep(3)
# print('This is printed after 3 seconds')
#
# time.sleep(3)
# print('This is printed after 3 more seconds')

#Python time.struct_time Class
#Several functions in the time module, such as gmtime(), asctime(), localtime(),
#and so on, either take or return the time.struct_time object. Python’s time.struct time is a class.
# Many time functions return values in time.struct_time format.
# The syntax of the time.struc_time object is as follows:
# time.struct_time(tm_year=2021, tm_mon=10, tm_mday=20,
#                     tm_hour=11, tm_min=40, tm_sec=17,
#                     tm_wday=4, tm_yday=301, tm_isdst=0)

#Python time.localtime()
#Let’s say we want to convert epoch time to local time and have the result be a struct time object.
# We could use either the localtime() or gmtime() functionalities to accomplish this.
# The localtime() function accepts as an input the amount of seconds since the epoch
# and returns struct time in local time. It allows us to access the various fields
# of a local time-stamp, such as the year, hour, seconds, and so on.

# import time
#
# result = time.localtime(seconds)
# print('Result:', result)
#
# print('\ntm_year:', result.tm_year)
# print('tm_hour:', result.tm_hour)
# print('tm_yday:', result.tm_yday)
#
# current_time=time.gmtime(seconds)
# print('Current Year:', current_time.tm_year)
# print('Month of the year:', current_time.tm_mon)
# print('Day of the month:', current_time.tm_mday)

#Python time.asctime()
#The asctime() method accepts struct time (or a tuple of 9 elements corresponding to struct time)
# #as an argument and returns a string representation of it.

# import time
# t=(2024, 11, 10, 11, 59, 0, 0, 0, 0)
# local_time=time.asctime(t)
# print ("Local time", local_time)

#Python time.strftime()
#The inverse of the time.strptime() method is time.strftime().
# It accepts struct time class tuples as arguments and returns a string indicating the time
# based on the supplied format codes. Assume we want to convert a struct time object to a
# string with the following format: Month/Day/Year and Hours/Minutes/Seconds.
# We could achieve such by using the following code:

# import time
# current_time=time.localtime() #get struct_time
# time_string= time.strftime('%m/%d/%Y , %H:%M:%S',current_time)
# print (time_string)

# Add time in Python-
#We make use of datetime.timedelta(hours) function in Python for adding time
# with hours set to the required added hours to convert hours to a datetime.timedelta object.
# Include the current datetime.datetime object containing the previous datetime.timedelta
# to generate a new datetime.datetime object with the extra hours.

# import datetime
# current_date_and_time=datetime.datetime.now()
# print ("Current data and time:")
# print (current_date_and_time)
#
# hours=5
# hours_added= datetime.timedelta(hours=hours)
# days_added = datetime.timedelta(days=5)
#
# future_date_and_time=current_date_and_time + hours_added
# print ("Future date and time: ")
# print (future_date_and_time)

# from datetime import datetime
# mydatetime= datetime(2024,10,25,16,55,5)
# print (type(mydatetime))
# print (mydatetime)
#
# mydatetime=mydatetime.replace(month=11)
# print (mydatetime)
#
# from datetime import date, datetime
# date1=date(2024,11,11)
# date2=date(2023,11,11)
# result=date1 - date2
# print (result.days )
# print (type(result))
#
# datetime1=datetime(2024,11,11,11,47,0)
# datetime2=datetime(2023,11,11,11,37,0)
#
# mydiff=datetime1 - datetime2
# print(mydiff.seconds)
# print (mydiff.total_seconds())

#===============================PRACTICE============================================#
# from collections import Counter
# my_list=[1,2,1,1,1,3,3,4,4,5,2,6]
# new_list=Counter(my_list)
# print (new_list)

#my_list=[1,2,1,1,1,3,3,4,4,5,2,6]
# my_set=set(my_list)
# print (list(my_set))
#
# new_list=[]
# [new_list.append(item) for item in my_list if item not in new_list]
# print (new_list)

# duplicate=None
# new_list=[]
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
#     else:
#         pass
# print (new_list)

#my_list=[27,9,15,30,6,12]
#my_list=sorted(my_list)
#my_list.sort()
#print (my_list)

# for i in range(len(my_list)):
#     for j in range(i + 1,len(my_list)):
#         if my_list[i] > my_list[j]:
#             my_list[i],my_list[j]=my_list[j],my_list[i]
# print (my_list)

# def factorial (number):
#     total = 1
#     for i in range(1, number):
#         total *= i
#     return total
# print (factorial(5))

# my_list=[27,9,15,30,6,12]
# largest=None
# for item in my_list:
#     if largest==None:
#          largest=item
#     elif item > largest:
#         largest=item
# print (f"The highest value:{largest}")
#=====================================================================================#
# import sys
# print (sys.prefix)
# import os
# print (os.environ.get('VIRTUAL_ENV'))

#======================================================================================
# MATH AND RANDOM MODULE
import math
#help(math)
# value=4.35
# floor=math.floor((value))
# print (floor)
# ceil=math.ceil(value)
# print (ceil)

# print (round(4.35))
# print (round(4.5))
# print (round(5.5))
#
# print (math.pi)
#Check numpy
# print (math.inf)
# print (math.nan)
# print ("Exponential",math.e)
# print ("Log",math.log(math.e))
# print ("Sin",math.sin(10))
# print ("Radians",math.radians(100))

#RANDOM
#The Python random seed() method is used to initialize the pseudo-random
#number generator of Python which generates the random values.
#If we specify or set the seed with a certain value it will generate the same value
# in all the executions of the program.
#The random number generator generates the random numbers in Python. But in many cases,
# we want that the random number generator to generate the same number(s) in each
# run for all the machines. So, we use the Python random seed() method.

import random
#print (random.randint(0,100))

# random.seed(101)
# print (random.randint(0,100))
# print (random.randint(0,100))
# print (random.randint(0,100))
# print (random.randint(0,100))
# print (random.randint(0,100))

# mylist= list(range(0,20))
# print (mylist)
# print (random.choice(mylist))

# SAMPLE WITH REPLACEMENT
#print (random.choices(population=mylist,k=10))
# SAMPLE WITHOUT REPLACEMENT
#print (random.sample(population=mylist,k=10))
#SHUFFLE
#Python API methods that alter a structure in-place generally return None,
# not the modified data structure.
# random.shuffle(mylist)
# print (mylist)

# UNIFORM
#print (random.uniform(a=10,b=100))

#GAUSS
#print (random.gauss(mu=0, sigma=1))
#==================================================================================================
# PYTHON DEBUGGER
#Instead of using print () we can use buit-in debugger tool that allows to interactively
# explore variable within mid-operation of our Python code.
# x= [1,2,3]
# y=2
# z=3
# result= y + z
#print (result)
#result2= x + y
#print (result2)

# import pdb # q to quit
# x= [1,2,3]
# y=2
# z=3
# result= y + z
# pdb.set_trace()
# result2=x + y
#======================================================================================
#PYTHON REGULAR EXPRESSIONS
# Regular expressions allow us to search for general patterns in text data.
# For example a simple email format can be : user@email.com
# We are looking for pattern text "text + "@" + "text" + ".com". We are looking for "@" and ".com"
# Use re library to search for patterns within text.

# text="The agent's phone number is 408-555-1234. Call soon!"
# print ('phone' in text)

import re
# pattern='phone'
# myregex1=re.search(pattern,text)
# print (myregex1)
# match=re.search(pattern,text)
# print(match)
# print (match.span())
# print (match.start())
# print (match.end())
# pattern = 'NOT IN TEXT'
# myregex2=re.search(pattern,text)
# print (myregex2)
#
# text="The agent's phone number is 408-555-1234. Call on this number soon!"
# matches=re.findall('number',text)
# print (matches)
# print (len(matches))
#
# for match in re.finditer('number',text):
#     #print (match)
#     print (match.group())

#Regular Expression patterns
#Character Identifiers
# Character  Description Example pattern code Example Match
#\d           A digit      file_\d\d           file_25
# \w           Alphanumeric  \w-\w\w\w          A-b_1
# \s         White Space     a\sb\sc            a b c
# \D         A non digit     \D\D\D            ABC
# \W        Non-alphanumeric  \W\W\W\W\W      *-+=)
# \S         Non white space  \S\S\S\S       Yoyo

# text="My phone number is 408-555-7777"
# phone=re.search('408-555-7777',text)
# print (phone)
# # 'r' tells Python that we are using \ as escape characters but as regular expressions.
# phone=re.search(r'\d\d\d-\d\d\d-\d\d\d\d',text)
# print (phone)
# print(phone.group())

#Quantifiers
# Character       Description            Example pattern code     Example Match
#      +     Occurs one or more times    Version \w-\w+       Version A-b1_1
#     {3}    Occurs exactly 3 times        \D{3}               abc
#    {2,4}   Occurs 2 to 4 times          \d{2,4}             123
#     {3,}     Occurs 3 or more          \w{3,}             anycharacters
#      *      Occurs zero or more times   A*B*C*               AAACC
#     ?        Once or none               plurals?            plural

# phone=re.search(r'\d{3}-\d{3}-\d{4}',text)
# print (phone)
#
# phone_pattern=re.compile('(\d{3})-(\d{3})-(\d{4})')
# results=re.search(phone_pattern,text)
# print(results.group(1))

#Additional REGEX syntax
# search=re.search(r'cat|dog','The cat is here')
# print (search)
#
# search_2=re.findall(r'..at','The cat in the hat went splat.')
# print (search_2)
#
# search_3=re.findall(r'^\d', "1 is a number.")
# print (search_3)
# search_4=re.findall(r'\d$', "Number ends with 2")
# print (search_4)

#phrase="there are 3 numbers 34 inside 5 this sentence"

#Exclude digits
# pattern=r'[^\d]+'
# print(re.findall(pattern, phrase))

# test_phrase="This is a string! But it has punctuation. How can we remove it?"
# clean=re.findall(r'[^].?!]+',test_phrase)
# print (''.join(clean))

# text="Only find the hypen-words in this sentence. But you do not know how long-ish they are"
# pattern=r'[\w]+'
# print(re.findall(pattern,text))
# pattern=r'[\w]+-[\w]+'
# print(re.findall(pattern,text))

# text="Hello, would you like some catfish?"
# texttwo="Hello,would you like to take a catnap?"
# textthree="Hello,have you seen this caterpillar?"

# print(re.search(r'cat(fish|nap|erpillar)',text))
# print(re.search(r'cat(fish|nap|erpillar)',texttwo))
# print(re.search(r'cat(fish|nap|erpillar)',textthree))

# TIMIMG YOUR PYTHON CODE.
# def func_one(n):
#     return[str(num) for num in range (n)]
# print (func_one(10))
#
# def func_two(n):
#     return list(map(str,range(n)))
# print (func_two(10))

#import time
#CURRENT TIME BEFORE
#start_time=time.time()
#RUN CODE
#result=func_one(1000000)
#result=func_two(10000)
#CURRENT TIME AFTER RUNNING CODE
#end_time=time.time()
#ELAPSED TIME
#elapsed_time=end_time - start_time
#print (elapsed_time)

# import timeit
# stmt='''
# func_one(100)
# '''
#
# setup='''
# def func_one(n):
#     return[str(num) for num in range (n)]
# '''
#
# result1=timeit.timeit(stmt,setup,number=100000)
# print (result1)
#
# stmt2='''
# func_two(100)
# '''
# setup2='''
# def func_two(n):
#     return list(map(str,range(n)))
# '''
# result2=timeit.timeit(stmt2,setup2,number=100000)
# print (result2)

# ZIP AND UNZIPPING FILES WITH PYTHON

f=open('fileone.txt','w+')
f.write('ONE FILE')
f.close()

f=open('filetwo.txt','w+')
f.write('TWO FILE')
f.close()

# import zipfile
#
# comp_file=zipfile.ZipFile('comp_file.zip','w')
# comp_file.write('fileone.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('filetwo.txt',compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()
#
# zip_obj=zipfile.ZipFile('comp_file.zip','r')
# zip_obj.extractall('extracted_content')

import shutil
dir_to_zip='C:\\Project_2024\\extracted_content'

output_filename='example'

shutil.make_archive(output_filename,'zip',dir_to_zip)

shutil.unpack_archive('example.zip','final_unzip','zip')



























