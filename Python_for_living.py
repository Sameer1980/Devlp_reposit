# print('Slope: %.2f' % 1.123)
#
# a = [(lambda x: x*10) (x) for x in range(10)]
# print (a)
import numpy as np

#STRING INTERPOLATION/ FORMATTING.
#Formatting with the format method.
print ("This is a string {}".format('INSERTED'))
print ('The {} {} {}'.format('fox','is','brown'))
#print ('The {} {} {}'.format('fox','brown','quick'))
print ('The {2} {1} {0}'.format('fox','brown','quick'))
print ('The {q} {b} {f}'.format(f='fox',b='brown',q='quick'))

#Float formatting follows "{value:width.precision f}"
result=100/777
print (result)
print ('The result was {r:1.5f}'.format(r=result))

result=104.12345
print (result)
print ("The result was {r:1.2f}".format(r=result))

# name='Jose'
# print (f'Hello, his name is {name}')
#
# name='Anshuk'
# age = 1.5
# print (f'{name} is {age} years old.')
#
# my_str='samir'
# print (my_str.capitalize())
# my_str='P' + my_str[1:]
# print (my_str)

# d={'K1':123,'k2':[0,1,2],'k3':{'insidekey':100}}
# print (d['k2'])
# print (d['k3']['insidekey'])
# print (d['k2'][2])
#
# d={'key1':['A','B','C','D']}
# print (type(d))
# print (d)
# l=[]
# l=d['key1']
# print (l)
# ll=l[3].lower()
# print (ll)
# l[3]=ll
# print (l)


# d1=d['key1'][0].lower()
# d['key1'][0]=d1
# print (d)


d={'key1':['a','b','c','d','e']}
d1=d['key1'][0].upper()
#print (d1)
d2=d['key1'][4].upper()
d3=d['key1'][2].upper()
d['key1'][0]=d1
#print (d)
d['key1'][4]=d2
d['key1'][2]=d3
print (d)


l1=[[2,3,8],[4,6,1]]
#print (l1)

print (l1[1])
print (l1[1][1])

myset=set()
myset.add(1)
print (myset)

myset.add(2)
print (myset)

myset.add(2)
print (myset)

mylist=[1,1,1,1,2,2,2,2,3,3,3,3,3]
print (mylist)
mylist=set(mylist)
print(type(mylist))
print (mylist)

print (type(True))

print (1>2)

b=None
print (b)

l1=[27,9,36,18]
l1.sort()
print (l1)

l1.reverse()
print (l1)

for i in range(1,len(l1)):
    print (i,l1[i])

for i in enumerate(l1,2):
    #print (type(i))
    print (i)

#Working with Files

myfile=open('myfile.txt')
#print (myfile.read())
#print (myfile.readlines())

# with open ('myfile.txt') as my_new_file:
#     contents=my_new_file.read()
#     print (contents)

# with open ('myfile.txt',mode='a') as f:
#     contents=f.write('\nthis is the fourth line')
#     #print (contents)

# with open ('myfile.txt') as my_new_file:
#     contents=my_new_file.read()
#     print (contents)

# with open ('newfile.txt',mode='w') as f:
#     f.write('I created this file!!')
#
# with open ('newfile.txt') as my_new_file:
#     contents=my_new_file.read()
#     print (contents)


# r=3 + 1.5 + 9
# print (r)
# print (type(r))
#
# r=(60 + (10 ** 2) / 4 * 7) - 134.75
# print (r)
#
# print ("Square" ,'->',10 ** 2)
# print ("Square root" ,'->' , 100 ** 0.5)

#Tough
d= {'k1' : [{'nest_key':['this is deep',['hello']]}]}
#print (d['k1'][0]['nest_key'][1][0])

#Tougher
d= {'k1' : [1,2,{'nest_key':['this is deep',['hello']]}]}
#print (d['k1'][2]['nest_key'][1][0])

#Toughest
d={'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
#print (d['k1'][2]['k2'][1]['tough'][2][0])

# print (1<2 and 2>3)
#
# print (100==1 or 2==2)
#
# print (1 == 1)
#
# print (not(1 == 1))
#
# my_list=[1,2,3,4,5,6,7,8,9,10]

# list_sum=0
# for num in my_list:
#     list_sum = num + list_sum
# print (list_sum)

#Tuple unpacking
#mylist=[(1,2),(3,4),(5,6),(7,8)]
#for item in mylist:
    #print (item)

#for a,b in mylist:
    #print (a)
    #print (b)

# mylist=[(1,2,3),(5,6,7),(8,9,10)]
#
# for a,b,c in mylist:
#     #print (a)
#     #print (b)
#     print (c)

# d={'k1':1, 'k2':2, 'k3':3}
# print (d)
# for key,value in d.items():
#     print (value)

# x=0
# while x < 5:
#  print (f"The current value of X is {x}")
#  x = x + 1
# else:
#     print ('X is not less than 5')

# x=[1,2,3]
# for _ in x:
#  pass
#
# print ("End of my script")

# for letter in 'SAMMY':
#     if letter == 'A':
#         continue
#     print (letter)

# x=0
# while x < 5:
#     if x == 2:
#         break
#     print(x)
#     x+=1

# word='abcde'
# for index , letter in enumerate (word):
#     print (index)
#     print (letter)
#     print ('\n')

#Using ZIP function.
# mylist1=[1,2,3,4,5,6]
# mylist2=['a','b','c']
# mylist3=[100,200,300]
#
# for item in zip(mylist1,mylist2,mylist3):
#     print (item)
# print (list(zip(mylist1,mylist2)))

# print ('x' in [1,2,3])
#
# print ('x' in ['x','y','z'])
#
# print ('a' in 'a world')

# print('mykey' in {'mykey': 345})
#
# d={'mykey': 345}
#
# print (345 in d.values())
# print (345 in d.keys())
#
# mylist=[10,20,30,40,100]
# print ("MINIMUM",'->',min(mylist))
# print ("MAXIMUM",'->',max(mylist))

#SHUFFLE

# from random import shuffle
# mylist=[1,2,3,4,5,6,7,8,9,10]
# #print ("Original list ->", mylist)
# shuffle(mylist)
# #print ("Shuffled List -> ", mylist)
#
# from random import randint
# print ("Random no.",'->',randint(0,100))
# mynum=randint(0,10)
# print(mynum)

#INPUT FUNCTION
# result=float(input('Favourite number?'))
# print (type(result))
# print (result)

#List Comprehension.
mystring='hello'
mylist=[word for word in mystring]


# for word in mystring:
#     mylist.append(word)
#print (mylist)

mylist=[x for x in 'word']
#print (mylist)

mylist=[num for num in range(1,11)]
#print (mylist)

mylist = [num**2 for num in range(1,11)]
#print (mylist)

mylist=[x for x in range(1,11) if x%2==0]
#print (mylist)

mylist=[x**2 for x in range(1,11) if x%2==0]
#print (mylist)

celsius=[0,10,20,34.5]
fahrenheit=[]

for temp in celsius:
    fahrenheit.append(((9/5) * temp + 32))
#print (fahrenheit)

fahrenheit=[((9/5) * temp + 32) for temp in celsius]
#print (fahrenheit)

results=[num if num%2==0 else 'ODD' for num in range(1,11)]
#print (results)

#Nested List Comprehension
# mylist=[]
# for x in [2,4,6]:
#     for y in [1,10,1000]:
#         mylist.append(x*y)
# print (mylist)

# mylist=[x*y for x in [2,4,6] for y in [1,10,1000]]
# print (mylist)

# st='Sam Print only the words that start with s in this sentence'
#
# for word in st.split():
#     if word[0].lower()=='s' or word[0]=='S':
#         print (word)
#
# mylist=[x for x in range(1,51) if x%3==0]
# print (mylist)

# mylist=[]
# st='Print every word in this sentence that has an even number of letters'
# for word in st.split():
#     if len(word)%2==0:
#         mylist.append(word)
# print (mylist)

#Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the number , and for the multiples of five print "Buzz" . For numbers which are
# multiples of both three and five print "Fizzbuzz"

# for num in range(1,101):
#     if num%3==0 and num%5==0:
#         print ("FizzBuzz")
#     elif num%3==0:
#         print ('Fizz')
#     elif num%5==0:
#         print ('Buzz')
#     else:
#         print (num)
#
st='Create a list of the first letter of every word in this string'
# mylist=[val[0] for val in st.split()]
# print (mylist)

# mylist=[]
# for val in st.split():
#     mylist.append(val[0])
# print (mylist)

#Count the number of 'i' s in a string.
# list1=[]
# count=int()
# for elm in st:
#     if elm=='i':
#         list1.append(elm)
#         count=list1.count('i')
# print ("Count of i ->",count)

#Doing the same with list comprehension.
# list1=[elm for elm in st if elm =='i']
# print (list1)
# print (list1.count('i'))

# str1='Samir Banerjee'
#
# for elm in range(len(str1)):
#     print (elm,'->',str1[elm])
# print ("Length of the String ->", len(str1))

#List comprehension to create a list of numbers divisible by 3.
list1=[idx for idx in range(1,50) if idx%3==0]
#print (list1)

#Go through the string below and if the length of a word is even print "even" !
st='Print every word in this sentence that has an even number of letters'

list1=st.split()
even_list=[elm for elm in list1 if len(elm)%2==0]
#print (even_list)

# Range of integers from 1 to 100. Multiple of 3 print "Fizz", multiple of 5 print "Buzz", Multiple of
#both 3 & 5 print "FizzBuzz"
# for idx in range(1,100):
#     if idx%3==0 and idx%5==0:
#         print ("FizzBuzz")
#     elif idx%3==0:
#         print ("Fizz")
#     elif idx%5==0:
#         print ("Buzz")
#     else:
#         print (idx)

# for idx in range(1,50):
#     print (idx)

#Use list comprehension to create a list of first letter of every word in the string below:
st="Create a list of the first letters of every word in this string"
list1=[elm[0] for elm in st.split()]
#print (list1)

#Methods and functions
# Return allows to save the results to a variable.

def say_hello(name='Default'):
    print (f'Hello {name}')

say_hello('Samir')
say_hello()

def add_num(n1,n2):
    return (n1 + n2)

#print (add_num(32,89))
#result=add_num(32,89)
#print (result)

def print_result(a,b):
    print (a + b)

def return_result(a,b):
    return a + b

result=print_result(21,90)
#print (result)

result=return_result(21,90)
#print ("Using return",result)

def sum_numbers(num1, num2):
    return num1 + num2

result=sum_numbers(32,40)
#print (result)

result=sum_numbers('32','40')
#print (result)

# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#         else:
#             pass
# print (check_even_list([2,9,3]))

# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#         else:
#             return False # WRONG !!
# print (check_even_list([9,2,3]))

# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#         else:
#              pass
#     return False     #CORRECT !!
# print (check_even_list([9,1,3]))

# def check_even_list(num_list):
#     # return all the even numbers in a list
#
#     #placeholder variables
#     even_numbers=[]
#
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#         else:
#             pass
#     return even_numbers
# print (check_even_list([1,2,3,4,5,6,7,8,9,10]))

# d1={'a':1,'b':2,'c':3,'d': 4}
# for key,val in d1.items():
#     print (key)
#     print (val)
#     print ('\n')

# Tuple unpacking with function.
# stock_prices=[('APPL',200),('GOOG',400),('MSFT',100)]
# # for items in stock_prices:
# #     print (items)
# for ticker , price in stock_prices:
#     print (price + (0.1 * price))

work_hours=[('Abby',100),('Billy',4000),('Cassie',800)]

# def employee_check (work_hours):
#     current_max=0
#     employee_of_month=''
#     for employee,hours in work_hours:
#         if hours > current_max:
#             current_max=hours
#             employee_of_month=employee
#         else:
#             pass
#     return(employee_of_month,current_max)
#
# print (employee_check(work_hours))
# result=employee_check(work_hours)
# print (result)
# name,hours=employee_check(work_hours)
# print (name)
# print (hours)

# list1=[8,1,24,16,10,39,28]
# list1.sort()
# print (list1)

# list1=[[8,10,2],[50,6,18],[39,13,26],[90,14]]
# #SORTED LIST
# for val in list1:
#   val.sort()
# print (list1)
# # HIGHEST VALUE
# curr_val=0
# for val1 in list1:
#     for val2 in val1:
#         if val2 > curr_val:
#             curr_val=val2
#         else:
#             pass
# print ("Highest value ->",curr_val)

# def highest_in_list():
#     curr_val=0
#     list1=[[8,101,2],[502,6,18],[39,1300,26],[90,14]]
#     for outer_list in list1:
#         for in_value in outer_list:
#             if in_value > curr_val:
#                 curr_val=in_value
#     return curr_val
#
# result=highest_in_list()
# print(f'Highest value -> {result}')

# def second_highest_in_list():
#     list1=[[8,10,2],[24,6,18],[39,13,26],[28,14]]
#     #SORTED LIST
#     for val in list1:
#         val.sort()
#     print (list1)
#     l1=[]
#     for inner in list1:
#         l1.append(inner[-2])
#     return l1
#     #print (list1)
#
#     #for val in list1:
#         #print (val[-2])
#
# res=second_highest_in_list()
# print (f'Second highest -> {res}')




# def highest_in_sublist():
#     list1=[[8,10,2],[24,6,18],[39,13,26],[28,14]]
#     print ('SORTED LIST')
#     list2=list1.sort()
#     return list2
#
#
# print (highest_in_sublist())

def word_select():
 st='Select all the words starting with the letter s or S'
 l1=st.split()
 l2=[]
 for letter in l1:
    if letter[0]=='S' or letter[0]=='s':
        l2.append(letter)
 return (l2)

res=word_select()
print (res)

def word_count():
    st='Count all the words in the string having letter "t"'
    count=0
    for letter in st:
        if letter == 'T' or letter =='t':
            count += 1
    return (count)

res=word_count()
print (f'The count of letters starting with "t" is -> {res}')

def first_letter_of_every_word():
 st="Create a list of the first letters of every word in this string"
 l2=st.split()
 l1=[]
 for letter in l2:
     l1.append(letter[0])
 return (l1)

res=first_letter_of_every_word()
print (f'List of the first letter of every word-->')
print (f'{res}')

# def highest_value_in_sublist():
#  list1=[[8,10,2],[24,6,18],[39,13,26],[28,14]]
#  l1=[]
#  for outer_list in list1:
#     outer_list.sort()
#     l1.append(outer_list[-1])
#  return(l1)
#
# res=highest_value_in_sublist()
# print (f'{res} ---> the list of highest values in sublist')

def highest_value_in_list():
    list1=[[8,100,2],[24,600,18],[39,13,26],[280,14]]
    curr_val=0
    for outer_list in list1:
      for inner in outer_list:
          if inner > curr_val:
              curr_val=inner
          else:
              pass
    return (curr_val)

res=highest_value_in_list()
print (f'{res} is the highest value in the list.')

# list1=[[8,10,2],[24,6,18],[39,13,26],[28,14]]
# for outer_list in list1:
#     outer_list.sort()
# print(list1)

def second_highest_value_in_sublist():
 list1=[[8,10,2],[24,6,18],[39,13,26],[28,14]]
 l1=[]
 for outer_list in list1:
     outer_list.sort()
     l1.append(outer_list[-2])
 return(l1)

res=second_highest_value_in_sublist()
#print (f'{res} ---> the list of second highest values in sublist')
#print (f'{res}')

#Interaction bettween Python functions
example=[1,2,3,4,5,6,7]
from random import shuffle
shuffle(example)

# def shuffle_list(mylist):
#     shuffle(mylist)
#     return mylist
# res=shuffle_list(example)
# print (res)
#
# mylist=['','O','']
# print (shuffle_list(mylist))

# def player_guess():
#
#     guess=''
#     while guess not in ['0','1','2']:
#         guess=input("Pick a number: 0, 1, or 2:-")
#     return int(guess)
#
# myindex=player_guess()

# def check_guess(mylist,guess):
#     if mylist[guess]=='O':
#         print("Correct!!")
#     else:
#         print ("Wrong guess!")
#         print (mylist)

# INITIAL LIST
mylist=['','O','']

# SHUFFLE LIST
#mixedup_list=shuffle_list(mylist)

#USER GUESS
#guess=player_guess()

# CHECK GUESS
#check_guess(mixedup_list,guess)


#** args & Kwargs
# def myfunc(a,b,c=0,d=0,e=0):
#     # Returns 5% of the sum of a and b.
#      return sum ((a,b,c,d,e)) * 0.05
#
# res=myfunc(40,60,100,100,3,4)
# print (res)

# ARGS RETURNS A TUPLE.
# def myfunc(*args):
#     print (args)

# def myfunc(*args):
#     print (args)
#     return sum(args) * 0.05
#
# # def myfunc(*spam):
# #     return sum(spam) * 0.05
#
# res=myfunc(40,60,100,1,34,16,19,22,21,90,15)
# print (res)

# KWARGS RETURNS A DICTIONARY.
# def myfunc(**kwargs):
#     print (kwargs)
#     if 'fruit' in kwargs:
#         print ('My fruit of choice is {}'.format(kwargs['fruit']))
#     else:
#         print ('I did not find any fruit here')
#
# myfunc(fruit='apple', veggie='lettuce',meat='mutton',fish='Hilsa')

# def myfunc(*args, **kwargs):
#     print (args)
#     print (kwargs)
#     print ('I would like {} {}'.format(args[0],kwargs['food']))
#
# print (myfunc(10,20,30,fruit='Orange',food='eggs',animal='dog'))


def myfunc(str):
    l1=[]
    for idx in range(len(str)):
        if idx%2==0:
            l1.append(str[idx].upper())
        else:
            l1.append(str[idx].lower())
    return l1

        # if val%2==0:
        #     return upper(args[val])
        # else:
        #     return lower(args[val])

res=myfunc('Samir')
print (res)

l1=[1,2,3,4,5,6]
l1.pop()
print (l1)

# 007 Game
def spy_game(nums):
    code=[0,0,7,'x']
    for num in nums:
        if num==code[0]:
            code.pop(0)
    return len(code)==1

res1=spy_game([1,2,4,0,0,7,5])
print (res1)

res2=spy_game([1,0,2,4,0,5,7])
print (res2)

res3=spy_game([1,7,2,0,4,5,0])
print (res3)

#Lambda expressions ,Map and Filter.

def square(num):
    return num**2

my_nums = [1,2,3,4,5]

for item in map(square,my_nums):
    print (item)

m_list=list(map(square,my_nums))
#print (m_list)

def splicer(mystring):
    if len(mystring)%2==0:
        return 'EVEN'
    else:
        return mystring[0]

names=['Andy', 'Eve', 'Sally']

l1=list(map(splicer,names))
print (l1)

def check_even(num):
    return num%2==0
mynums=[1,2,3,4,5,6]

l1=list (filter(check_even,mynums))
#print (l1)

# for n in filter(check_even,mynums):
#     print (n)


# mylist1=[1,2,3,4,5,6]
# mylist2=['a','b','c']
# mylist3=[100,200,300]
#
# for item in zip(mylist1,mylist2,mylist3):
#     print (item)
# #print (list(zip(mylist1,mylist2,mylist3)))

# STEP BY STEP - LAMBDA EXPRESSION
#Step 1:
def square(num):
    result=num ** 2
    return result

myint=square(3)
print (myint)

#Step2:
def square(num):
    return num ** 2

myint=square(3)
print (myint)

#Step3: Lambda is anonymous function to be used only once. Hence we don't give it a name.
def square(num):return num ** 2

#Lambda expression
#lambda num : num ** 2
square=lambda num : num ** 2
print (square(5))

mynums=[1,2,3,4,5,6]
l1=list(map(lambda num: num ** 2,mynums))
print (l1)

l1=list(filter(lambda num: num%2==0,mynums))
print (l1)

print (names)

l1=list(map(lambda s: s[0],names))
print (l1)

#REVERSE
l1=list(map(lambda x: x[::-1],names))
print (l1)

#Nested Statements and scope.

#x=25

# def printer ():
#     x = 50
#     return x

#print (x)

# L E G B
#L- LOCAL
#E - ENCLOSING
# G - GLOBAL
# B - BUILTIN

#LOCAL -> num variable
# lambda num : num ** 2

# 1) --> LOCAL
# name= 'THIS IS A GLOBAL STRING'
#
# def greet():
#     name= 'Sammy'
#
#     def hello():
#         print ('Hello ' + name)
#     hello()
# print (greet())
#
# # 2) --> ENCLOSING
# def greet():
#     #name= 'Sammy'
#
#     def hello():
#         print ('Hello ' + name)
#     hello()
# print (greet())

# 3) --> GLOBAL

#GLOBAL
# name= 'THIS IS A GLOBAL STRING'
#
# def greet():
#     #ENCLOSING
#     name= 'Sammy'
#
#     def hello():
#         #LOCAL
#         name='IM A LOCAL'
#         print ('Hello ' + name)
#     hello()
# print (greet())

# X=100
# def func(x):
#     print (f'X is {x}')
#
#     # LOCAL REASSIGNMENT
#     x=200
#     print (f'I JUST LOCALLY CHANGED X TO {x}')
#
# print (X)
# print (func(50))

#x=50

# def func():
#     global  x
#     print (f'X is {x}')
#
#     # LOCAL REASSIGNMENT TO A GLOBAL VARIABLE !!
#     x= 'NEW VALUE'
#     print (f' I JUST LOCALLY CHANGED GLOBAL X TO {x}')
#
# print (x)
# print (func())
# print (x)

#DISPLAYING INFORMATION
# VALIDATING USER INPUT
#Python isdigit() function returns a Boolean value TRUE if all the values in the input string
# are digits; else it returns FALSE. The Python isdigit() string method is used to check
# if all the characters in the string are digit values or not.
#

# def user_choice():
#     choice=input("Please enter a number (0-10)")
#     return int(choice)
#
# res=user_choice()
# print (res)

# value='two'
# print (value.isdigit())

# def user_choice():
# #VARIABLES
#
# # Initial
#  choice='WRONG'
#  acceptable_range=range(0,10)
#  within_range=False
#
# #TWO CONDITIONS TO CHECK
# #DIGIT OR WITHIN_RANGE == FALSE
#  while choice.isdigit()==False or within_range==False:
#     choice=input("Please enter a number (0-10): ")
# # DIGIT CHECK
#     if choice.isdigit()==False:
#         print ("Sorry that is not a digit!!")
#
# # RANGE CHECK
#     if choice.isdigit() == True:
#          if int(choice) in acceptable_range:
#              within_range=True
#          else:
#             print ("Sorry you are out of acceptable range(0-10)")
#             within_range=False
#
#  return int(choice)
#
# res=user_choice()
# print (res)

#OBJECT ORIENTED PROGRAMMING
# SELF keyword connects methods/ attributes to the object or instance of a  class.
# It represents the instance of the object itself.

class Dog():
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR ANY INSTANCE OF A CLASS
    # CLASS ATTRIBUTE
    species='mammal'
    # CREATING INSTANCE ATTRIBUTE
    def __init__(self,breed,name,spots):
        # Attributes
        # We take in the arguement.
        # Assign it using self.attribute_name
        self.breed=breed
        self.name=name
        # Expect boolean True / False
        self.spots=spots

      # OPERATIONS / ACTIONS --- > Methods
    def bark(self,number ):
          print ("WOOF! My name is {} and the number is {}".format(self.name,number))

my_dog=Dog(breed='Lab',name='Frankie',spots='SPOTS')
#my_dog=Dog()

print (type(my_dog))
print (my_dog.breed)
print (my_dog.name)
print (my_dog.spots)
print (my_dog.species)
print (my_dog.bark(10))

my_another_dog=Dog(breed='Lab',name='Jammie',spots='SPOTS')
# -----------------------------------------------------------------------------
#------------------------------------------------------------------------------

# myset=set(['a','b','c','d','e'])
# myset[2]='M'
# print (myset)
# newset=set(['c','e','d','f'])
# print (type(myset))
# #res=myset.union(newset)
# #res=myset.intersection(newset)
# res=newset.difference((myset))
# mylist=list(res)
# mylist.sort()
# print (mylist)
#------------------------------------------------------------------------------

# class Circle():
#   # CLASS OBJECT ATTRIBUTE
#   pi= 3.14
#   def __init__(self,radius=1):
#       self.radius=radius
#       self.area= radius * radius  * Circle.pi
#
#   #METHOD
#   def get_circumference(self):
#          return self.radius * Circle.pi * 2

# my_circle=Circle(30)
# print (my_circle.radius)
# print (my_circle.pi)
# print (my_circle.area)
# print (my_circle.get_circumference())

# INHERITANCE AND POLYMORPHISM
# class Animal():
#     def __init__(self):
#         print ("ANIMAL CREATED")
#     def who_am_i(self):
#         print ("I am an animal")
#     def eat(self):
#         print ("I am eating")

# myanimal=Animal()
# print (myanimal.who_am_i())
# print (myanimal.eat())

# class Dog(Animal):
#     def __init__(self):
#         print ("Dog Created")
#     def eat(self):
#         print ("I am a dog and eating")
#     def bark(self):
#         print ("WOOF!")
#
# mydog=Dog()
# print (mydog.who_am_i())
# print (mydog.eat())
# print (mydog.bark())

# POLYMORPHISM(optional)
# class Dog():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return self.name + " says Woof!"
#
# class Cat():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#         return self.name + " says Meow!"
#
# nico= Dog("niko")
# felix=Cat("felix")
# print (nico.speak())
# print (felix.speak())
#
# for pet in [nico,felix]:
#     print (type(pet))
#     print (pet.speak())
#
# def pet_speak(pet):
#     print (pet.speak())
#
# print (pet_speak(nico))
# print (pet_speak(felix))

# ABSTRACT CLASS AND METHOD.

# class Animal():
#     def __init__(self,name):
#         self.name=name
#     def speak(self):
#        raise NotImplementedError("Subclass must implement this abstract class")
#
# class Dog(Animal):
#     def speak(self):
#         return self.name + " says Woof!!"
#
# class Cat(Animal):
#     def speak(self):
#         return self.name + " says Meow!!"
#
# fido=Dog("Fido")
# isis=Cat("Isis")
# print (fido.speak())
# print (isis.speak())

# SPECIAL MAGIC / DUNDER METHODS.

#check the length of a list.
# mylist=[1,2,3]
# print (len(mylist))
#
# class Book():
#     def __init__(self,title,author,pages):
#         self.title= title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return f"{self.title} by {self.author}"
#     def __len__(self):
#         return self.pages
#     def __del__(self):
#         print ("A book object has been deleted.")

#b=Book("Python for Beginers", 'Samir', 300)
# When you give print (b) Python searches for a string representation str(b).Both return same.
# But with Magic methods we can give a new definition to str(b)
#print (b)
#print (str(b))
# With MAgic method __len__(self) we can return the length of the BOOK class object
# which otherwise would have returned error.

#del b
#print(len(b))


#Use del to delete variables from computer's memory.
# print (del b) returns error but with Magic method
#del b
#print (b)

#--------------------------------------------------------------------------------

# mystr='Narcissist'
# pos1=mystr.find('s')
# print (mystr[pos1].upper())
# mystr=mystr[0:pos1] + mystr[pos1].upper() + mystr[pos1 + 1:]
# print (mystr)
#------------------------------------------------------------------------------------
#MODULES AND PACKAGES.
#PyPI is a repository for open-source third party Python packages similar to NPM for Node.js

# from colorama import Fore
# print (Fore.RED + 'some red text')
# print (Fore.GREEN + 'Switch to green')
#print (Fore.WHITE)

# Modules are just .py scripts that you can call in another .py script.
# Packages are a collection of modules.
# In order to enable Python to treat folders/ directories as Package create a file
# __init__.py
#----------------------------------

# l1=[8,16,32]
# l2=[5,15,20]
# output = l1 + l2
# print (output)
#-------------------------------------

#  __name__ and "__main__"

# __name__ is a built in variable
# __name__ = "__main__" -- Python runs it in the background whether we invoke it or not.

# ERROR AND EXCEPTION HANDLING.
# TRY - THIS IS THE BLOCK OF CODE TO BE ATTEMPTED (MAY LEAD TO AN ERROR)
# EXCEPT - BLOCK OF CODE WILL EXECUTE IN CASE THERE IS AN ERROR IN TRY BLOCK.
# FINALLY - A FINAL BLOCK OF CODE TO BE EXECUTED , REGARDLESS OF AN ERROR.

# def add (n1,n2):
#     print (n1 + n2)

# number1= 10
# number2= input ("Please provide a number: ")
# addops=add(number1,number2)

# try:
#     # WANT TO ATTEMPT THIS CODE
#     # MAY HAVE AN ERROR
#     #result= 10 + 10
#     #result= 10 + '10'
#     #print (result)
#
# except:
#     print ("Hey it looks you aren't adding correctly!")
# else:
#     print ('Add went well!')
#     print (result)

# try:
#     f=open('testfile','w')
#     f.write("write a test line.")
# except TypeError:
#     print ("There was a type error!!")
# except OSError:
#     print ("Hey you have an OS Error !")
# finally:
#     print ("I always run")

# try:
#     f=open('testfile','r')
#     f.write("write a test line.")
# except TypeError:
#     print ("There was a type error!!")
# except OSError:
#     print ("Hey you have an OS Error !")
# except:
#     print ("All other exceptions!")
# finally:
#     print ("I always run")

# try:
#     x = int(input("Enter a number: "))
#     y = 10 / x
#     print ("The result is", y)
# except ValueError:
#     print ("You must enter a valid integer.")
# except ZeroDivisionError:
#     print ("You cannot divide by zero.")

# def ask_for_int():
#     while True:
#      try:
#         result=int(input("Please provide number: "))
#      except:
#         print ("Whoops! That is not a number")
#         continue
#      else:
#         print ("Yes Thank You!")
#         break
#      finally:
#          print ("I am going to ask you again!!")
#         # print("End of try/except/finally")
#         # print ("I will always run at the end!")

# def ask_for_int():
#     while True:
#      try:
#         result=int(input("Please provide number: "))
#      except:
#         print ("Whoops! That is not a number")
#         continue
#      else:
#         print ("Yes Thank You!")
#         break
#
# ask_for_int()

# UNIT TESTING
# --> PYLINT AND UNITTEST
#PYLINT -> This is a library that looks at your code and reports back possible issues.
#UNITTEST -> This built-in library will allow to test your own programs and check you are getting
# desired outputs.

#PYLINT -> Use Pylint to check your code for possible errors and styling.
# Python has a set of style convention rules known as "PEP 8".

# Use PYLINT instead of python when executing the script from the command line.
# EG: > pylint simpleone.py
# Look out for any error starting with a 'E' .














