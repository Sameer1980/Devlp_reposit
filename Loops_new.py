# n=5
# while n>0:
#     print (n)
#     n=n-1
# print ('Blastoff!')
import sys

# x=5
# if x>2:
#     print ('Bigger than 2')
#     print ('Still bigger')
# print('Done with 2')

# for i in range(5):
#     print(i)
#     if i>2:
#         print ('Bigger than 2')
#     print ('Done with i',i)
# print ('All Done')

# inp=input('Europe Floor?')
# usf=int(inp)+1
# print ('Us Floor',usf)

# x=42
# if x>1:
#     print ('more than 1')
#     if x< 100:
#         print ('less than 100')
# print ('All done')

# x=20
# if x< 2:
#     print ('Small')
# elif x<10:
#     print ('Medium')
# else:
#     print ('Large')
# print ('All Done')

# x=5
# if x<2:
#     print ('small')
# elif x<10:
#     print ('medium')
# print ('All done')

# def exampleif(x1):
#  x2=x1
#  if x2<2:
#     return 'small'
#  if x2<10:
#     return 'medium'
#  if x2<20:
#     return 'big'
#  elif x2<40:
#     return 'large'
#  elif x2<100:
#     return 'Huge'
#  else:
#     return 'Ginoromous'
#
# print (exampleif(100))

# x=100
# if x<2:
#     print ('Below 2')
# if x<20:
#     print('Below 20')
# if x<10:
#     print ('Below 10')
# else:
#     print ('Something else')

# str='Hello Bob'
# try:
#     int1=int(str)
# except:
#     istr=-1
#     print ('First',istr)


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
# #
# x=addtwo(999999.20,1)
# print (x)

# Loop does not run at all!!

# n=0
# while n>0:
#     print ('Lather')
#     print ('Rinse')
#     print ('Dry off!!')

# Breaking out of a loop.

# while True:
#     line=input('> ')
#     if line == 'done':
#         break
#     print (line)
# print('Done!')

# The continue statement ends the current iteration and jumps to the top of the loop
# and starts the next iteration.

# while 1:
#     line =input(':= ')
#     if line=='#':
#         continue
#     if line=='done':
#         break
#     print (line)
# print('Done!')

# for i in [5,4,3,2,1]:
#     print (i)

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

# for rec in [24,16,19,20]:
#      print (rec)

# a = [3, 2]
# a=[i-1 for i in a]
# print(a)

#Counting in a loop
# zork=0
# print ('Before',zork)
# for thing in [9,41,12,3,74,15]:
#     zork=zork+1
#     print (zork,thing)
# print('After',zork)

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

# count=0
# sum=0
# for value in [9,41,12,3,74,15]:
#     count=count+1
#     sum=sum+value
# print (f"Average: {sum}/{count}")

# count=0
# sum=0
# for value in [90,21,15,0,103,82]:
#     count=count+1
#     sum=sum + value
# print ("Count-", count ,"," "Sum-", sum,"," "Value-",value)
# print ("Average(sum/count):", sum/count)

# Filtering in a loop.
# print('Before')
# for value in [9,41,12,3,74,15]:
#     if value > 20:
#         print ('Larger than 20', value)
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
# list1=[10,35,20,99,41,32,16,0,1,8]
# for num in enumerate (list1,1):
#     print (num)
# print ("Length",len(list1))

# enum=enumerate(list1,1)
# print (type(enum))
# for _,val in enum:
#  print (_,val)

# tup1=(10,35,20,99,41,32,16,0,1,8)
# print (type(tup1))
# for _,num in enumerate(tup1,1):
#     print (_,num)
# print ("Length",len(tup1))

# print (sys.prefix)
# import os
# print (os.environ.get('VIRTUAL_ENV'))

# dict1={"a":"India","b":"Pakistan","c":"Bangladesh","d":"Sri Lanka","e":"Nepal","f":"Afghanistan","g":"Myanmar"}
# print(type(dict1))
# # print(dict1)
# for _,elm in enumerate(dict1,1):
#     print (elm)

# set1={"India","Pakistan","Bangladesh","SriLanka","Nepal","Afghanistan","Myanmar","Maldives","Bhutan"}
# print ("Length",len(set1))
# print ("Type",type(set1))
# print (set1)
# for _,elm in enumerate(set1,1):
#  print (_,elm)

# list2=["India","Pakistan","Bangladesh","SriLanka","Nepal","Afghanistan","Myanmar","Maldives","Bhutan"]
# print (list2)

# list4=[10,35,40.29,999.3,0,1,'Johny',{"Age":42}]
# print (list4)
# print(type(list4))

# list3=[10,35,20,99,41,32,16,0,1,8]
# for _ in range(0,len(list3)-2, 2):
#     print (_,list3[_])
# print("Length of list",len (list3))

# For loop in Tuple.
# new_tup=tuple()
# new_tup=(10,35,40.29,999.3,0,1,'Johny',{"Age":42})
# for _ in range(len(new_tup)):
#     print(_,new_tup[_])
# print("Length of tuple", len(new_tup))

# s='Python'
# print("Length",len(s))
#
# for ind in reversed (range(len(s))):
#     print (ind,s[ind])

# str1='SAMIR'
# for i in range(len(str1)):
#     print (i,str1[i])
# print (list(range(2)))
# print (list(range(0,5)))

# str='SAMIR'
# rvstr=str[::-1]
# print (rvstr)

# dict2={"a":1,"b":2,"c":3,"e":4,"f":5}
# dict2={k:v*2 for (k,v) in dict2.items()}
# print (dict2)

#list1=[5,10,15,20,25,30,35,40,45,50]
# list1.reverse()
# print (list1)

# list2=[5,30,40,35,15,10,50,25,20,45]
# list2.sort()
# print(f"Sorted:",list2)
#
# for idx1 in range(len(list2)):
#     for idx2 in range(idx1 + 1,len(list2)):
#         if list2[idx1]>list2[idx2]:
#             list2[idx1],list2[idx2]=list2[idx2],list2[idx1]
# print ("Sorted Ascending-", list2)

# list3=[5,30,40,35,15,10,50,25,20,45]
# list3.sort(reverse=True)
# print ("Sorted Descending:",list3)
#
# for idx1 in range(len(list3)):
#     for idx2 in range(idx1 + 1,len(list3)):
#         if list3[idx1]<list3[idx2]:
#             list3[idx1],list3[idx2]=list3[idx2],list3[idx1]
# print ("Sorted Descending-", list3)




#For loop in dict.
# new_dict=dict()
# new_dict={"Name":"Samir","Age":42,"InsuranceID":"XXXXXXX12569","Salary":80000,"ROI":12.2}
# for k in new_dict:
#     print (k,'->',new_dict[k])
# for val in new_dict.items():
#     print (val)
# print ("Length of dict",len(new_dict))
# for val in new_dict:
#     print (val,new_dict[val])

# set2={'Samir',42,'XXXXXX12569',80000,12.2}
# print (type(set2))
# for i in range(len(set2)):
#     print (i,set2[i])
# for i in enumerate(set2,1):
#     print (i)

# print ("Using Range")
# list1=[0,700114,400709]
# print ("Length -",len(list1))
# print ("Using normal FOR LOOP.")
# for _ in list1:
#     print (_)
# print ("Using RANGE in FOR LOOP.")
# for i in range(len(list1)):
#     print (i,'->',list1[i])
# print ("Using ENUMERATE in FOR LOOP.")
# for elm in enumerate(list1,1):
#      print (elm)

# dict1={1:'A',2:'B',3:'C',4:'D'}
# print("Length",'->',len(dict1))
# print ("Type",'->',type(dict1))
# print (dict1)
# for elm in dict1:
#     print (elm,'->',dict1[elm])
#
# print ("Using ITEMS function.")
# for elm in dict1.items():
#     print (elm)

# set2={1,3,5,7,9,11,13}
# print ("Length",'->',len(set2))
# print ("Type",'->',type(set2))
# print (set2)
# for elm in set2:
#     print (elm)
# for elm in range(len(set2)):
#     print (elm,'->',set2)
# for elm in enumerate(set2,1):
#     print (elm)

# for elm in [15,21,90,700114,400709,'Ryback']:
#     print (elm)


# str_obj='Hello World'
# for _ in range(len(str_obj)):
#     print (_,str_obj[_])

# complx_dict=dict()
# complx_dict={"Name":"Samir","Age":42,"Salary":80000,"details":{"ConsumerID":"CON_92475_T","InsuranceID":"XXXXXXX12569","Premium":10000,"ROI":8.2}}
# #print ("Insurance details-",complx_dict['details'])
# print ("Insurance ID-",complx_dict['details']['InsuranceID'])
# #print ("Using split", complx_dict['details']['InsuranceID'].split())
# print("Transformation on Insurance ID-",complx_dict['details']['InsuranceID'].split('X')[-1])
#for val in complx_dict.items():
   #print (val)
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

# a=['foo', 'bar', 'baz']
# itr=iter(a)
# print (itr)
# print (type(itr))
# print (tuple(itr))
# print (next(itr))

# numbers=[12, 34, 1, 4, 4, 67, 37, 9, 0, 81]
# res=[]
# for elm in range(len(numbers)):
#     if numbers[elm]>5:
#         res.append(numbers[elm])
# print (res)

# SET Operations
# set1={'A',1,'CC',9,'E','J','K','O',0,'Z'}
# set2={'BB','A',8,9,'Z',1,13,21,15,90}
#print ("UNION - ",set1.union(set2))
# print ("INTERSECTION - ",set1.intersection(set2))

# for elm in set1:
#     print (elm)
# set3=set1.union(set2)
# res=[]
# for elm in set3:
#     res.append(elm)
# print (type(res))
# print ("Listed (UNION)- ",res)

# set4=set1.intersection(set2)
# res1=[]
# for elm in set4:
#     res1.append(elm)
# print(type(res1))
# print ("Listed (INTERSECTION) - ",res1)

# set5=set1.difference(set2)
# res2=[]
# for elm in set5:
#     res2.append(elm)
# print ("Listed (DIFFERENCE) - ", res2)

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

#list1=[10,35,20.99,41,32,16,0.1,8,'Ramirez',[249,999999.9,'Gotcha'],('a','xyz',{'Name':'Sanchez'}),{'Age':92,'ROI':349.1}]
# print ("Length - ",len(list1))
# list1.append([32,64,128])
# print (list1)
# list1.extend([32,64,128])
# print (list1)
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

# data_samples=[]
# for i in range(5):
#     sample_features={"feature1":i,"feature2":i*2,"feature3":i+3}
#     data_samples.append(sample_features)
#     #print (sample_features)
# print (sample_features)


# real_time_data=[]
# for time_stamp in range(0,100,10):
#     sensor_reading=time_stamp
#     real_time_data.append(sensor_reading)
# print (real_time_data)

# res4=[]
# res5=[]
# for s in 'samir':
#     res4.append(s)
#     res5.extend(s)
# print ("With APPEND",res4)
# print ("With EXTEND", res5)

# list1=[9,18,27,36]
# list2=[45,54,63,72,81]
# list3=[]
# list1.append(list2)
# print (list1)
# list1.extend(list2)
# print (list1)
# list1.append('SAMIR')
# print (list1)
# list1.extend('SAMIR')
# print (list1)
# for elm in list1:
#    print (elm)

#list2=[9,18,27,36,45,54,63,72,81,90]
# list2.pop()
# print (list2)
# list2.reverse()
# print (list2)
# pos=list2.index(81)
# print ("Index Position is - ",pos)
# print (list2)
# list2.pop(5)
# print (list2)
# list2.insert(5,36)
# print (list2)
# #print (list2.index())
# print (list2)
# list2.insert(4,'Samir')
# print (list2)
# list2[9]='Banerjee'
# print (list2)
# list2.pop()
# print (list2)
# list2.append(9)
# print (list2)
# list2.insert(9,'Banerjee')
# print (list2)
# list2.pop()
# print (list2)
# list2.append(9)
# print (list2)
# list2.pop(9)
# print (list2)
# list2.pop(4)
# print (list2)
# list2.sort()
# print (list2)
# list2_cp=list2.copy()
# print ("Original list:", list2)
# print ("Copy of original list",list2_cp)
# list2_cp.clear()
# print (list2_cp)

# print (list2)
# list2.append(90)
# print (list2)
# tup1=()
# tup1=tuple(list2)
# print (type(tup1))
# print (tup1)
# tup1.pop()
# print (tup1)
#tup1.insert(4,'Samir')
# print (tup1)
# print (tup1[10])
# tup1[10]=0
# print (tup1)

# dict1={"Assignment1": 100, "Assignment2": 100, "Assignment3":100, "Assignment4": 100}
# print (type(dict1))
# #print (dict1)

# for elm in dict1.items():
#    print (elm)

# for elm in dict1:
#    print (elm ,'->' ,dict1[elm])

# for elm in dict1.values():
#    print ("Values: ",elm)

# for elm in dict1.keys():
#    print ("Keys:", elm)

# for elm in dict1:
#    print (elm ,'->', dict1[elm])
# n=5
# while n>0:
#     print (n)
#     n=n-1
# print ('Blastoff!')
import sys
# n=5
# while n>0:
#    print (n)
#    n=n-1
# print ('Blastoff!')

#Reverse
# list4=[11,22,33,44,55,66,77,88,99,110]
# # list4.reverse()
# # print (f"Reversed:,{list4}")
#
# R=list4[::-1]
# print (f"Reversed:,{R}")

# str='SAMIR'
# R=str[::-1]
# print (R)

#Nested for loop.
# adj= ["green", "leafy", "juicy"]
# vegetables = ["spinach", "kale", "pumpkin"]
# for x in adj:
#     for y in vegetables:
#         print (x,y)

# def ascending():
#  list2=[9,90,27,54,36,45,81,63,72,18]
#  for elm0 in range(len(list2)):
#      for elm1 in range(elm0+1,len(list2)):
#        if list2[elm0]>list2[elm1]:
#          list2[elm0],list2[elm1]=list2[elm1],list2[elm0]
#  #print (list2)
#  return list2
#
# print ("Sorted List:" , ascending())
# def descending():
#    list2=[9,90,27,54,36,45,81,63,72,18]
#    for elm0 in range(len(list2)):
#       for elm1 in range(elm0+1,len(list2)):
#          if list2[elm0]<list2[elm1]:
#             list2[elm0],list2[elm1]=list2[elm1],list2[elm0]
#    return (list2)
#
# print ("Sorted list (descending)", descending())
# def square(x):
#    return x * x
#
# print (square(4))

# def strexample(st1):
#  str1=''
# #print (type(str))
#  try:
#   str1=st1
#   for i in range(len(str1)):
#    #print (i,str1[i])
#     if str1[i]=='M':
#       str1[i]='m'
#  except:
#     return "String object is immutable"
#
# print ("Raising exception on string:", strexample('SAMIR'))

# str='Hello Bob'
# try:
#     int1=int(str)
# except:
#     istr=-1
#     print ('First',istr)

# def largest(x):
#   try:
#     largest_so_far=None
#     list3=[9,90,27,54,36,45,1,81,63,72,18]
#     x1=x
#     if x1==isinstance(x1,str):
#       raise Exception
#     list3.append(x1)
#     for idx in range(len(list3)):
#       if largest_so_far==None:
#        largest_so_far=list3[idx]
#       elif list3[idx]>largest_so_far:
#         largest_so_far=list3[idx]
#     return largest_so_far
#   except:
#     return "ERR- Input must be a numeric."
#
#
# print ("Largest so far!!", largest('x'))

# def smallest():
#    list3=[9,90,27,54,36,45,1,81,63,72,18,0]
#    smallest_so_far=None
#    for elm in range(len(list3)):
#       if smallest_so_far== None:
#          smallest_so_far=list3[elm]
#       elif list3[elm]<smallest_so_far:
#           smallest_so_far=list3[elm]
#    return smallest_so_far
#
# print ("Smallest so far!!", smallest())

# list1=[9,18,27,36,45,54,63,72,81]
# list1.reverse()
# print ("Using reverse function:", list1)
#
# list1=[9,18,27,36,45,54,63,72,81]
# R=list1[::-1]
# print ("Reversed list using object notation-", R)
#
# print (list1[1:6])
# print (list1[::2])


# def fileops_read(fl_name):
#     with open (fl_name,"r") as file_hndl1:
#         read_content=file_hndl1.read()
#         return read_content
#
# print (fileops_read('TEST.txt'))

# def fileops_write(fl_name):
#     with open (fl_name,"a") as file_hndl1:
#         write_content=file_hndl1.write("\n Line 6: Test line for WRITE 2.")
#         return write_content
#
# print (fileops_write('TEST.txt'))

# def fileops_write(file_name):
#     with open (file_name,'w') as file_hdl:
#         write_return= file_hdl.write("New file opened for Write Operation.\n Line 1: Test line for WRITE 1.")
#         return write_return
# print (fileops_write('TEST2.txt'))

# def fileops_append (file_name):
#     with open (file_name,'a') as file_hdl:
#         write_return=file_hdl.write("\n Line 2: Test line for WRITE 2.")
#         return  write_return
#
# print (fileops_append('TEST2.txt'))

# LIST COMPREHENSION.
# square=[]
# for idx in range (10):
#     square.append(idx * idx)
# print (square)

# def squares():
#     square=[idx * idx for idx in range(10)]
#     return square
#
# print ("Square: ",squares())

# def even_number():
#     even_num=[num for num in range(1,21) if num%2==0]
#     return even_num
# print ("Even Series - 1st 10 numbers", even_number())

# def odd_number():
#     odd_num=[num for num in range(20) if num%2!=0]
#     return odd_num
#
# print ("Odd Series - 1st 10 numbers", odd_number())

# def factorial (number):
#     total = 1
#     for i in range(1, number):
#         total *= i
#     return total
# print ("Factorial result: ", factorial(5))

# def factorial (p1):
#     result=1
#     fact=[result := result * i for i in range(1,p1)]
#     return result
# print ("Factorial result: ",factorial(6))

# name='Carol'
# age=35
# print (f"{name} is {age} years old." )

#F String format
# product="Python Course"
# price=99.9
# print (f"{product} costs ${price}")
# def list_comprehension():
#     grt_than=[i for i in range(1,51,5) if i>25]
#     return grt_than
# print ("Greater than: ", list_comprehension())

#fibonacci sequence
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

# def fibonacci(num):
#     a=1
#     b=1
#     if num>0:
#         print (a)
#         print (b)
#         for i in range(2,num):
#          c=a+b
#          a=b
#          b=c
#          print (c)
# fibonacci(10)

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
# print(fibonacci(10))

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
# print (type(data))
# atpos=data.find('@')
# print (atpos)
# sspos=data.find(' ',atpos)
# print (sspos)
# host=data[atpos+1:sspos]
# #print (type(host))
# print (host)

#data='Luthra, Shivani <shivani.a.luthra@capgemini.com>; on behalf of; IN, Architects Desk <architectsdesk.in@capgemini.com>'
# print (type(data))
# # pos1=data.find('Shivani')
# # print (pos1)
# # pos2=data.find('Luthra')
# # name=data[pos2:pos1]
# # print (name)
# pos3=data.find()

#Demonstrator on how to use split () , find() and strip () functions.
# data='Luthra, Shivani <shivani.a.luthra@capgemini.com>; on behalf of; IN, Architects Desk <architectsdesk.in@capgemini.com>'
# tags=data.split()
# print (tags)
# # stp1=tags[2].lstrip('<')
# # print (stp1)
# sm_col_rem=tags[2].rstrip(';')
# #print (sm_col_rem)
# pos1=data.find('<')
# pos2=data.find('>',pos1)
# email=data[pos1+1:pos2]
# print (f"Email : {email}")
# name=tags[1] + ' ' +tags[0].rstrip(',')
# print (f"Name : {name}")
# #tag_rem_dl_right=tags[9].rstrip('>')
# tag_rem_dl_right=tags[9]
# #print (sm_col_rem_dl_right)
# tag_rem_dl_left=tags[9].lstrip('<')
# #print (sm_col_rem_dl_left)
# pos3=tag_rem_dl_right.find('<')
# pos4=tag_rem_dl_right.find('>',pos3)
# #sprint (pos4)
# DL_email=tag_rem_dl_right[pos3+1:pos4]
# print (f"DL Email ID: {DL_email}")
# #email=stp1+stp2
# #print (email)

# line='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
# words=line.split()
# print (words)
# email=words[2]+' '+words[3]+' '+words[4]+' '+words[5]+' '+words[6]
# print (email)
# email=words[1]
# print (email)
# piece1=email.split('@')
# # piece2=email.split('.')
# print (piece1[0])

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

#

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

# Dictionary Comprehension
# dict1={'a':1, 'b':2,'c':3,'d':4,'e':5}
# double_dict1={k:v*2 for (k,v) in dict1.items()}
# print (double_dict1)

# counts=dict()
# names=['csev','cwen','csev','zqian','cwen','zqian','csev','Samir']
# for name in names:
#     counts[name]=counts.get(name,0)+1
# print (counts)
#
# counts['Justin']=2
#
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


# import pyodbc
# cnxn = pyodbc.connect(r'Driver=SQL Server;Server=HP-PC\SQLEXPRESS;Database=AdventureWorks2012;Trusted_Connection=yes;')
# print (type(cnxn))
# cursor = cnxn.cursor()
# cursor.execute('select * from dbo.department')
# #
# for row in cursor:
#    # print ('row=%r'%(row,))
#     print(row[0], ' - ', row[1] + ' - ' + row[2], ' - ', row[3])

#list2=['Peter Parker','Alan B Walker', 'Bruce Wayne','Tony Stark','Clark Kent']
# for elm in list2:
#     print (elm)
# for idx in range(len(list2)):
#     print (idx,'->',list2[idx])

# def enum():
#   print ("Using ENUMERATE")
#   ret_val=list()
#   for elm in enumerate(list2):
#    ret_val=elm
#    print (ret_val)
# enum()

#DICT COMPREHENSION
# dict1={"a":1,"b":2,"c":3,"d":4,"e":5}
# dict2= {k:v*2 for k,v in dict1.items()}
# print (dict2)

#LIST COMPREHENSION
# def square():
#     list1=[idx*idx for idx in range(1,10)]
#     return list1
# print ("Squared:",square())

# def even (x):
#   print ("Even Number Series:")
#   even_val=[num for num in range(1,x) if num%2==0]
#   return even_val
# print (even(21))

#LAMBDA
# greet=lambda name: "Hello " + name
# #print (type(greet))
# print (greet("Samir"))




