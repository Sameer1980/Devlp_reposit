#Matching and extracting data.
# import re
# x = 'My favourite 2 numbers are 19 and 42'
#  y = re.findall('[0-9]+',x)
# print (y)
#
# y=re.findall('[AEIOU]+',x)
# print (y)

'''x='From: Using the : character'
y=re.findall('^F.+:',x)
print (y)'''

'''x='From: Using the : character'
y=re.findall('^F.+?:',x)
print (y)'''

#Python sockets
'''import  socket
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org',80))'''

#JSON
# import json
# data='''{
#     "name" : "Chuck",
#     "phone" : {
#         "type" : "intl",
#         "number" : "+1 734 303 4456"
#       },
#       "email" : {
#           "hide":"yes"
#       }
# }'''
# info = json.loads(data)
# print ("Name:", info["name"])
# print ("Hide", info["email"]["hide"])
# print ("Number:",info["phone"]["number"])

# Data base connectivity
# import pyodbc
#
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server=HP-PC\SQLEXPRESS;'
#                       'Database=AdventureWorks2012;'
#                       'Trusted_Connection=yes;')
#
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM HumanResources.Department')
#
# for i in cursor:
#     print (i)

#JSON
# import json
# input= '''[
#     { "id" : "001",
#        "x": "2",
#        "name":"Chuck"
#     },
#      { "id": "009",
#         "x":"7",
#         "name":"Chuck"
#       }
#      ]'''
#
# info= json.loads(input)
# print ('User Count:', len(info))
# for item in info:
#     print ("Name:",item['name'])
#     print("ID:",item['id'])
#     print ("Attribute",item['x'])