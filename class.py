# class dog:
#     def __init__(self,dogbreed,dogeyecolor) :
#         self.breed=dogbreed
#         self.eyecolor=dogeyecolor

# class address:
#     def __init__(mine,street,number) :
#         mine.street=street
#         mine.number=number

#     def myfunc(mine):
#       print ("My address is:", mine.street)
#       print ("Number: ", mine.number)

# # p1=address("Albert Street",20)
# # p1.myfunc()

# p1=address("Albert Street",20)
# p1.myfunc()

# class Fruits:
#     def __init__(self,*args):
#         self.type=args[0]
#         self.color=args[1]

#     def describe(self):
#         print ("This fruit is a {} {}".format(self.color,self.type))

# f1=Fruits('apple','red')
# f1.describe()

#print ("Hello world")

# class MyName:
#     def __init__(self,'Nathan') :
#         self.name='Nathan'

#     def my_name(self):
#         return self.name
    
# p2=MyName()
# p2.my_name()

# class DemoClass:
#     def sample_method(self):
#         print ("This is the demo method.")

# p2=DemoClass()
# p2.sample_method()
# print (dir(p2))

# def myfun(*args):
#     for arg in args:
#         print (arg)

# myfun("Hello","Welcome","to","my","house")

# class car():
#     def __init__(self,*args) :
#         self.model=args[0]
#         self.color=args[1]
#     def func1 (self):
#         print ("The car model is {} and color is {}".format(self.model,self.color))

# c1=car('BMW','black')
# c1.func1 ()

# def adder(*num):
#     sum=0
#     for n in num:
#         sum=sum+n
#     print ("Sum:",sum)

# adder(1,2,3,4,5,6,7,8,9,10)

# class Myclass:
#     def __init__(self , name , age):
#         self.name=name
#         self.age=age
#     def display_info(self):
#         print (f"Name:{self.name}")
#         print (f"Age:{self.age}")

# obj=Myclass("Samir",43)
# obj.display_info()

# class teacher:
#     def __init__(self,name,subject):
#         self.name=name
#         self.subject=subject
#     def show(self):
#         print ("{} teaches {}".format (self.name,self.subject))
# T1=teacher('Preeti Srivastava','Computer Science')
# T1.show()

# class teacher:
#     def __init__(self,*args):
#         if len(args)==1 & isinstance(args[0],str):
#             self.name=args[0]
#         elif len(args)==2:
#             self.name=args[0]
#             self.sub=args[1]
#         elif isinstance(args[0],int):
#             self.strength=args[0]


# t1=teacher("Preeti Srivastava")
# print ("{} is the name of the teacher".format(t1.name))
# t2=teacher("Preeti Srivastava","Computer Science")
# print (f"{t2.name} is the teacher for {t2.sub}")
# t3=teacher(32)
# print (f"Strength of the class is {t3.strength}")

# class car:
#     def __init__(self,*args):
#         self.speed=args[0]
#         self.color=args[1]
#         self.model=args[2]
#     def show(self):
#         print (f"Speed of the car is: {self.speed}")
#         print (f"Color of the car is:  {self.color}")
#         print (f"Model of the car is: {self.model}")
 
# audi= car(200,'red','Audi')
# audi.show()
# bmw= car (250,'black','BMW')
# bmw.show()
# # mb=car (190,'white')

# class car ():
#     def __init__(self,**kwargs):
#         self.speed=kwargs['s']
#         self.color=kwargs['c']

# audi=car (s=200, c='red')
# bmw= car (s=250,c='black')
# mb=car (s=190,c='white')

# print (audi.color)
# print (bmw.speed)

# def intro (**kwargs):
#     print ("\n Data type of arguement:", type(kwargs))

#     for key, value in kwargs.items():
#       print ("{} is {}".format(key,value))

# intro(Firstname="Samir", Lastname="Banerjee",Age=43,Phone=9874666307)

#INHERITANCE
class person (object):
    def __init__(self,*args) :
        self.name=args[0]
        self.ph_no=args[2]
        print ("Initialising the name attribute.")
class teacher(person):
    def __init__(self, *args):
        person.__init__(self,*args) #calling init of base class
        self.age=args[1]
        print ("Age attribute of base class is initilaised")

    def show(self):
        print ("Name of the teacher is", self.name)
        print ("Age of the teacher is:", self.age)
        print ("Phone:",self.ph_no)
t=teacher("Allen Park",45,9874666307) # the init of the subclass is called
t.show()




            