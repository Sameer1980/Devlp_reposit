'''n=5
while n>0:
    print (n)
    n=n-1
print ('Blastoff!')'''


'''x=5
if x>2:
    print ('Bigger than 2')
    print ('Still bigger')
print('Done with 2')'''

'''for i in range(5):
    print(i)
    if i>2:
        print ('Bigger than 2')
    print ('Done with i',i)
print ('All Done')'''

'''inp=input('Europe Floor?')
usf=int(inp)+1
print ('Us Floor',usf)'''

# x=42
# if x>1:
#     print ('more than 1')
#     if x< 100:
#         print ('less than 100')
# print ('All done')

'''x=20
if x< 2:
    print ('Small')
elif x<10:
    print ('Medium')
else:
    print ('Large')
print ('All Done')'''

'''x=5
if x<2:
    print ('small')
elif x<10:
    print ('medium')
print ('All done')'''

'''x=100
if x<2:
    print ('small')
if x<10:
    print ('medium')
if x<20:
    print('big')
elif x<40:
    print ('large')
elif x<100:
    print ('Huge')
else:
    print ('Ginoromous')'''

'''x=100
if x<2:
    print ('Below 2')
if x<20:
    print('Below 20')
if x<10:
    print ('Below 10')
else:
    print ('Something else')'''

'''str='Hello Bob'
try:
    int1=int(str)
except:
    istr=-1
    print ('First',istr)'''


# astr='Bob'
# try:
#     print ('Hello')
#     istr=int(astr)
#     print ('There')
# except:
#     istr=1
# print ('Done', istr)

# rawstr=input('Enter a number:')
# try:
#     ival=int(rawstr)
# except:
#     ival=-1
# if ival>=0:
#     print ('Nice work')
# else:
#     print('Not a number')

# print ('All even series:')
# for i in range(21):
#     if i==0:
#         i=i+1
#     if i%2==0:
#         print(i)

# print ('All odd series:')
# for i in range(20):
#     if i%2!=0:
#         print(i)

# def thing():
#     print ('Hello')
#     print('Fun')
# thing()
# print ('Zip')
# thing()

# big=max('Hello world')
# print(big)

# def greet(lang):
#     if lang=='es':
#         return 'Hola'
#     elif lang=='fr':
#         return 'Bonjour'
#     else:
#         return 'Hello'
# print (greet('es'),'Glenn')
# print (greet('fr'),'Glenn')

# def addtwo (a,b):
#     added=a+b
#     return (added)
#
# x=addtwo(999999.20,1)
# print (x)

# Loop does not run at all!!

# n=0
# while n>0:
#     print ('Lather')
#     print ('Rinse')
#     print ('Dry off!!')

# Breaking out of a loop.

'''while True:
    line=input('> ')
    if line == 'done':
        break
    print (line)
print('Done!')'''

# The continue statement ends the current iteration and jumps to the top of the loop
# and starts the next iteration.

# while True:
#     line =input('> ')
#     if line[0]=='#':
#         continue
#     if line=='done':
#         break
#     print (line)
# print('Done!')

'''for i in [5,4,3,2,1]:
    print (i)'''

# Finding the largest number.

# largest_so_far=None
# print ('Before',largest_so_far)
# for the_num in [9,41,12,3,74,15]:
#     if largest_so_far is None:
#         largest_so_far=the_num
#     elif the_num>largest_so_far:
#         largest_so_far=the_num
#     print(largest_so_far,the_num)
#
# print('After',largest_so_far)

#Counting in a loop
'''zork=0
print ('Before',zork)
for thing in [9,41,12,3,74,15]:
    zork=zork+1
    print (zork,thing)
print('After',zork)'''

# Summing in a loop
# zork=0
# print ('Before',zork)
# for thing in [9,41,12,3,74,15]:
#     zork=zork+thing
#     print(zork,thing)
# print('After',zork)

# Finding the average in a loop

# count=0
# sum=0
# print ('Before',count,sum)
# for value in [9,41,12,3,74,15]:
#     count=count+1
#     sum=sum+value
#     print (count,sum,value)
# print('After',count,sum,sum/count)

# Filtering in a loop.
# print('Before')
# for value in [9,41,12,3,74,15]:
#     if value > 20:
#         print ('Larger number', value)
# print('After')

# Search using a Boolean variable.
# found=False
# print ('Before',found)
# for value in [9,41,12,3,74,15]:
#     if value == 74:
#         found = True
#     else:
#         found = False
#     print (found,value)
# print('After',found)

#Printing value with index.Enumerate

#For loop in List.
# list=[10,35,20,99,41,32,16,0,1,8]
# for _,num in enumerate (list):
#     print (_,num)
# print ("Length",len(list))

# list=[10,35,20,99,41,32,16,0,1,8]
# for _ in range(len(list)):
#     print (_,list[_])
# print("Length of list",len (list))

# For loop in Tuple.
# new_tup=tuple()
# new_tup=(10,35,40.29,999.3,0,1,'Johny',{"Age":42})
# for _ in range(len(new_tup)):
#     print(_,new_tup[_])
# print("Length of tuple", len(new_tup))

#For loop in dict.
# new_dict=dict()
# new_dict={"Name":"Samir","Age":42,"InsuranceID":"XXXXXXX12569","Salary":80000,"ROI":12.2}
# for val in new_dict:
#     print (val,'->',new_dict[val])
# for val in new_dict.items():
#     print (val)
# print ("Length of dict",len(new_dict))

# str_obj='Hello World'
# for _ in range(len(str_obj)):
#     print (_,str_obj[_])

# complx_dict=dict()
# complx_dict={"Name":"Samir","Age":42,"Salary":80000,"details":{"ConsumerID":"CON_92475_T","InsuranceID":"XXXXXXX12569","Premium":10000,"ROI":8.2}}
# for val in complx_dict.items():
#    print (val)
# print ("Insurance details-",complx_dict['details'])
# print ("Insurance ID-",complx_dict['details']['InsuranceID'])
# print("Transformation on Insurance ID-",complx_dict['details']['InsuranceID'].split('X')[-1])
# if complx_dict['details']['ConsumerID'] is not None:
#     print ("Consumer ID-",complx_dict['details']['ConsumerID'])
# else:
#     print ("The type of complx_dict is",type(complx_dict))
# print ("Transformation on consumer ID-",complx_dict['details']['ConsumerID'].split('_')[-2])

#print ("Dictionary values",complx_dict)
#print ("Length of dictionary",len(complx_dict))

#Slicing an object.
# a = ("a", "b", "c", "d", "e", "f", "g", "h")
# for _ in range(len(a)):
#     print (_,a[_])
# x = slice(3, 5)
# print(a[x])
# x = slice(0, 8, 3)
# print(a[x])

# list1=[10,35,20.99,41,32,16,0.1,8,'Ramirez',[249,999999.9,'Gotcha'],('a','xyz',{'Name':'Sanchez'}),{'Age':92,'ROI':349.1}]
# print ("Length of the list:",len(list1))
# for _ in range(len(list1)):
#   print (_,list1[_])
#Extract list from within list.
#for record in list1:
   # if isinstance(record,list):
   #    print (type(record))
   #    print (record)
# Extract dict from within list.
#     if isinstance(record,dict):
#        print (record)
# #  Extract float from within list.
#     if isinstance(record,float):
#        print (record)
# Extract int from within list.
#    if isinstance(record,int ):
#        print (record)
#Extract tuple from within list.
     # if isinstance(record,tuple):
     #    print (record)

# list1=[10,35,20.99,41,32,16,0.1,8,'Ramirez',[249,999999.9,'Gotcha'],('a','xyz',{'Name':'Sanchez'}),{'Age':92,'ROI':349.1}]
# #list1.append([32,64,128])
# #list1.extend([32,64,128])
# list2=[]
# for _ in range(len(list1)):
#     print (_,list1[_])
# list1.extend([32,64,128])
# for _ in range(len(list1)):
#    print(_, list1[_])
# for x in list1:
#  list2.append(x)
# for _ in range (len(list2)):
#     print ("List1 appended-",_,list1[_])
#     print ("List2 appended-",_,list2[_])
#     print("List1 extended-", _, list1[_])
#     print("List2 extended-", _, list2[_])
#     print ("List1-->",list1)
#     print ("List2-->",list2)
# print ("List1---->",list1)
# print("List2---->",list2)

#Nested for loop.
# adj= ["green", "leafy", "juicy"]
# vegetables = ["spinach", "kale", "pumpkin"]
# for x in adj:
#     for y in vegetables:
#         print (x,y)

# Read a json file.
'''import  json
#f_handler=open('___extracted.json')
#data=json.load(f_handler)
#print (type(data))
with open("___extracted.json","r") as read_content:
    output=json.load(read_content)
    if output['audit']['taskId'] is not null:
        print (output['audit'][0]['taskId'])'''
#for record in data:
 #   print (record)

# Finding the smallest value.

# smallest = None
# print('Before')
# for value in [9, 41, 12, 3, 74, 15]:
#     if smallest is None:
#         smallest = value
#     elif value < smallest:
#         smallest = value
#     print(smallest, value)
# print('After', smallest)

# data='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# atpos=data.find('@')
# print (atpos)
# sspos=data.find(' ',atpos)
# print (sspos)
# host=data[atpos+1:sspos]
# print (host)

# List are mutable
# try:
#     fruit='Banana'
#     fruit[0]='b'
# except:
#     print ('String is immutable!!')
# x=fruit.lower()
# print (x)
# lotto=[2,14,26,41,63]
# print (lotto)
# lotto[2]=28
# print (lotto)

# total=0
# count=0
# while True:
#     try:
#         inp=input('Enter a number:')
#         if inp=='done' : break
#         value=float(inp)
#         print ("Value--",value)
#         total+=value
#         print ('Total--',total)
#         count+=1
#         print (count)
#     except:
#         print ('please enter a numeric value or done.' )
# average=total/count
# print ('Average:',average)

# numlist=list()
# while True:
#    try:
#     inp=input("Enter a number:")
#     if inp=='done' : break
#     value=float(inp)
#     numlist.append(value)
#    except:
#         print ('Please enter a numeric value or "done"')
#
# average=sum(numlist)/len(numlist)
# print ('Average:', average)

# Double split pattern

# line='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words=line.split()
# email=words[2]+' '+words[3]+' '+words[4]+' '+words[5]+' '+words[6]
# print (email)
# email=words[1]
# print (email)
# pieces=email.split('@')
# print (pieces[0])

# Empty dictionary
# ddd=dict()
# ddd['age']=21
# ddd['course']=182
# print (ddd)
# ddd['age']=23
# print (ddd)

#You can make an empty dictionary using empty curly braces
'''ooo={}
print (ooo)
jjj={'chuck':1,'fred':42,'jan':100}
print (jjj)'''

# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name]=counts[name]+1
# print (counts)

# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     counts[name]=counts.get(name,0)+1
# print (counts)

'''l=list()
dir(l)
#print (dir(l))

t=tuple()
dir(t)
print (dir(t))'''

#Tuples
# (x,y)=(4,'Fred')
# print (y)
#
# (a,b)=(99,98)
# print (a)

# d={'a':10,'b':1,'c':22}
# print ("Items-->",d.items())
# print(sorted(d.items()))

#Python dictionaries --- word count
# counts=dict()
# print ('Enter a line of text:')
# line = input('')
# words=line.split()
#
# print ('Words:',words)
# print ('Counting...')
# for word in words:
#     counts[word]=counts.get(word,0)+1
# print ('Counts',counts)


# numlist=list()
# while True:
#    try:
#     inp=input("Enter a number:")
#     if inp=='done' : break
#     value=float(inp)
#     numlist.append(value)
#    except:
#         print ('Please enter a numeric value or "done"')
#
# try:
#     average=sum(numlist)/len(numlist)
#     print ('Average:', average)
# except:
#     print ("Value entered is a string!!")

# counts={'chuck':1,'fred':42,'jan':100}
# for key in counts:
#     print (key , counts[key])

# name= input ('Enter file:')
# handle = open(name)
#
# counts=dict()
# for line in handle:
#     line=line.rstrip()
#     words=line.split()
#     print (words)
#     for word in words:
#         counts[word]=counts.get(word,0)+1
# print ('Counts--',counts)

'''fname=input('Enter file: ')
if len(fname)<1 : fname='clown.txt'
hand=open(fname)

di=dict()
for line in hand:
    line=line.rstrip()
    #print (line)
    word=line.split()
    #print (word)
    for w in word:
        oldcount=di.get(w,0)
        print (w,'old',oldcount)
        newcount=oldcount+1
        di[w]=newcount
        print (w,'new',newcount)
print (di)'''

#Tuples
'''y=(1,9,2)
for iter in y:
    print (iter)'''

'''(x,y)=(4,'Fred')
print (y)

(a,b)=(99,98)
print (a)'''

# Tuples and Dictionaries.
# d=dict()
# d['csev']=2
# d['cwen']=4
# for (k,v) in d.items():
#     print (k,v)
# tups=d.items()
# print (type(tups))
# print (tups)

# d={'a':10,'b':1,'c':22}
# print (d.items())
# print(sorted(d.items(),reverse=True))

# d={'a':10,'b':1,'c':22}
# t=sorted(d.items())
# print(t)
# for k,v in sorted(d.items()):
#     print (k,v)

#Sort by value instead of key
# c={'a':10,'b':1,'c':22}
# tmp=list()
# for k,v in c.items():
#     tmp.append((v,k))
# print (tmp)
# tmp=sorted(tmp,reverse=True)
# print (tmp)


# fhand=open('clown.txt')
# counts=dict()
# for line in fhand:
#     line=line.rstrip()
#     words=line.split()
#     print (words)
#     for word in words:
#       counts[word]=counts.get(word,0)+1
# print ("Counts ",counts)
#
# lst=list()
# for key , val in counts.items():
#     newtup=(val,key)
#     lst.append(newtup)
#
# lst=sorted(lst,reverse=True)
#
# for val, key in lst[:10]:
#     print (key,val)

#Shorter version
# c={'a':10,'b':1,'c':22}
# print (sorted([(v,k) for k,v in c.items()]))

# Working with HTML
'''import urllib.request,urllib.parse,urllib.error
fhand=urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#fhand=urllib.request.urlopen('https://en.wikipedia.org/wiki/Python')
counts=dict()
for line in fhand:
    #print (line.decode().strip())
    words=line.decode().split()
    for word in words:
        counts[word]=counts.get(word,0)+1
print (counts)'''

# count={}
# text=input('Enter text--')
# words=text.rstrip()
# words=text.split()
# print (words)
# for word in words:
#     count[word.casefold()]=count.get(word.casefold(),0)+1 # casefold() ignores case.
# print ('Count of words: ',count)

# Palindrome & list slicing--- Reversing any string , list or any iterable.
# def isPalindrome(s):
#     return s == s[::-1]
#
# s = input ('Enter string----')
# if s=='':
#     raise ValueError("Please enter a string value.")
# ans = isPalindrome(s)
# if ans:
#     print("It's a Palindrome.")
# else:
#     print("It's not a Palindrome.")
# Get every second value between 4th and 8th element of the list.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# part = nums[3:8:2]
# print(part)

# Slice the whole list.
# nums = [1, 2, 3, 4, 5, 6, 7]
# part = nums[::]
# print(part)

# Get every second value from a list without a start and stop but specify a step.
# nums = [1, 2, 3, 4, 5, 6, 7]
# part = nums[::2]
# print(part)

#The [::-1] Part
# nums = [1, 2, 3, 4, 5, 6, 7]
# part = nums[::-1]
# print(part)
# print ('Hello!!')

# fibonacci sequence
# def fib(n):
#     a=1
#     b=1
#     if n > 0:
#         print (a)
#         print (b)
#         for i in range (2,n):
#             c = a + b
#             a = b
#             b = c
#             print (c)
#     else:
#         print ('Please enter positive values')
# fib(10)

# fibonacci sequence generating recursive function  using lru cache and Memoization
# from functools import lru_cache
# @lru_cache(maxsize=1000)
# def fibonacci(n):
#     # check that the input is a positive integer .
#     if type(n) != int:
#         raise TypeError ("n must be a postive int")
#     if n < 1:
#         raise ValueError (" blah bla bla")
# # compute the nth term
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci (n-1) + fibonacci (n-2)
#
# for n in range (1,10):
#     print (fibonacci(n))

# def factorial (number):
#     total = 1
#     for i in range(1, number):
#         total *= i
#     return total
# print (factorial(5))