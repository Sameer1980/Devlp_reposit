# Python has decorators that allow you to tack on extra functionality to an already existing
# functionality.

# They use the @ operator and are then placed on top of the original function.

# Now you can easily add on extra functionality with a decorator.

# @some_decorator
# def simple_func():
#     # Do simple stuff
#     return something

def func():
    return 1

def hello():
    return 'Hello!'

#print (hello())

#greet=hello
# print (type(greet))
# print (greet())

# Functions are objects that can be passed to other objects.

del hello

#print (greet())

# def hello(name='Samir'):
#     print ("The hello() function has been executed!")
#     def greet():
#         return '\t This is the greet() function inside hello!'
#     def welcome():
#         return '\t This is welcome() inside hello!'
#     print (greet())
#     print (welcome())
#     print ('This is the end of the hello function!')
#
# hello()
#
# # Cannot be called from outside the main function.
# welcome()

#Function returning a function.
# def hello(name='Samir'):
#     print ("The hello() function has been executed!")
#     def greet():
#         return '\t This is the greet() function inside hello!'
#     def welcome():
#         return '\t This is welcome() inside hello!'
#     print ("I am going to return a function!!")
#
#     if name =='Samir':
#         return greet
#     else:
#         return welcome
#
# #FUNCTION Assigned to a VARIABLE
# my_new_func=hello()
# print (type(my_new_func))
# print (my_new_func())

# def cool():
#     def super_cool():
#         return 'I am very cool!'
#
#     return super_cool()
#
# some_func=cool()
# print (type(some_func))
# print (some_func)

#FUNCTION PASSED AS PARAMETER .
    # def hello():
    #     return 'Hi Jose!'
    #
    # def other (some_def_func):
    #     print ("Other code runs here!")
    #     print (some_def_func())
    #
    # other(hello)

# DECORATOR (USES BOTH THE ABOVE FEATURES - FUNCTION RETURNING A FUNCTION & FUNCTION PASSED AS PARAMETER.
#1)
# def new_decorator(original_func):
#     def wrap_func():
#         print ("Some extra code before the original function")
#         original_func()
#         print ("Some extra code after the original function!")
#
#     return wrap_func

# def func_needs_decorator():
#     print ("I want to be decorated!!")

#func_needs_decorator()

#new_decorator(func_needs_decorator)
#print (type(decorated_func))
#decorated_func

#2) A Better way !!

# @new_decorator
# def func_needs_decorator():
#     print ("I want to be decorated!!")
#
# print (type(func_needs_decorator))
# func_needs_decorator()

# When we call the decorated function actually the wrapper function executes !!

#GENERATORS
# Generator function allows us to write a function that can send back a value and then later resume
# to pick up where it left off.
# Generators are a type of function that allow us to generate a sequence of values over time.
# The main difference in syntax will be the use of yield statement.
# When a generator function is compiled they become an object that supports an iteration protocol.
# That means when they are called in your code they don't actually return a value and then exit.
# Generator function will automatically suspend and resume their execution and state around the last point
# of value generation.
# The advantage is that instead of having to compute an entire series of values up front , the generator
# computes one value and waits until the next value is called for.

# For example the range() function doesn't produce an list in memory for all the values from start to stop.
# Instead it just keeps track of the last number and the step size , to provide a flow of numbers.
# KEYWORDS - YIELD , NEXT() , ITER().
# Creating and storing the list in memory.
#
# def create_cubes(n):
#     result=[]
#     for x in range(n):
#         result.append(x ** 3)
#     return result

# print (create_cubes(10))
#
# for x in create_cubes(10):
#     print (x)

# We don't have the list in memory . Values are yielded or getting generated as and when required.
# So it is more memory efficient.
# def create_cubes(n):
#     for x in range(n):
#         yield x ** 3
# #
# print (create_cubes(10))
# print (list(create_cubes(10)))
# for x in create_cubes(10):
#     print (x)

# FIBONACCI SERIES USING GENERATOR . MORE MEMORY EFFICIENT .
# def gen_fibon(n):
#     a=1
#     b=1
#     for i in range (n):
#         yield  a
#         a,b=b,a + b
#
# for number in gen_fibon(10):
#     print (number)

# FIBONACCI SERIES USING NORMAL FUNCTION . LESS MEMORY EFFICIENT .
# def gen_fibon(n):
#     a=1
#     b=1
#     output=[]
#     for i in range (n):
#         output.append(a)
#         a,b=b,a + b
#     return output
# for number in gen_fibon(10):
#     print (number)

# def simple_gen():
#     for x in range(3):
#         yield x
# #
# print (type(simple_gen))
# for num in simple_gen():
#      print (num)

# Generator object does it internally using 'NEXT' when using the 'YIELD' keyword.It remembers the last
# value and generates the next sequential value. It does not store the list of values in memory.
# FOR loop catches the 'StopIteration' error and stops calling NEXT .
# g=simple_gen()
# print (type(g))
# print (g)
# print (next(g))
# print (next(g))
# print (next(g))
# print (next(g))

# l = ['Sarah', 'Roark', 30]
# for item in l:
#   print(item)

#To carry out the iteration this for loop describes, Python does the following:
# a)Calls iter() to obtain an iterator for l.
# b) Calls next() repeatedly to obtain each item from the iterator in turn.
# c)Terminates the loop when next() raises the StopIteration exception.

# s='hello'
# # for letter in s:
# #     print (letter)
#next(s)

# s_iter=iter(s)
# print (type(s_iter))
# print (next(s_iter))
# print (next(s_iter))
# print (next(s_iter))
# print (next(s_iter))
# print (next(s_iter))
# print (next(s_iter))

#iter() is a Python built-in function that returns an iterator object,
# which is an object that represent some data. For example, it could be used with a .next() method
# on the iterator that will give you the next element -
#StopIteration will occur when there are no more elements.

# def gensquares(N):
#     for i in range(N):
#       yield i ** 2
#
# print (type(gensquares))
# for x in gensquares(10):
#     print (x)

# import random
# def rand_num(low,high,n):
#     for i in range(n):
#      yield  random.randint(low,high)
#
# for num in rand_num(1,10,12):
#     print (num)

# s='hello'
# s=iter(s)
# print (next(s))
# print (next(s))

# Generator Comprehension
# my_list=[1,2,3,4,5]
# gencomp=(item for item in my_list if item > 3)
# print (type(gencomp))
#
# for item in gencomp:
#     print (item)
