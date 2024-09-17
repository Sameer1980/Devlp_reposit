list1 = ['Peter Parker', 'Bruce Wayne', 'Tony Stark', 'Clark Kent', 'Dr. Strange', 'Bruce Banner',
         'Steven Grant Rogers']


# print ("Length:",len(list1))

# def list_shape():
#  new_list=list()
#  print ("Length:",len(list1))
#  print ("Elements of list:")
#  for elm in list1:
#      new_list=elm
#      print(new_list)
# list_shape()

# def enumerate_list():
#     print ("Length:",len(list1))
#     print ("Elements of list:")
#     for elm in enumerate(list1,1):
#         print (elm)
# enumerate_list()

# for _ in range(len(list1)):
#     print (_,'->',list1[_])

# Dict Comprehension
# def dict_comp():
#  dict1={"A":1,"B":2,"C":3,"D":4,"E":5}
#  comprehension_result={k:v*2 for k,v in dict1.items()}
#  return comprehension_result
#
# print (dict_comp())

# LIST COMPREHENSION

# def even_series(x):
#     list_even=[i for i in range(1,x) if i%2==0]
#     return list_even
#
# print ("Even Series:", even_series(21))

# def factorial(x):
#     val=1
#     for i in range(1,x):
#         val=val*i
#     return val
# print ("Factorial value:",factorial(6))

# def fibonacci(n):
#   a = 1
#   b = 1
#   if n < 0:
#        print("Please enter positive values.")
#   elif n > 0:
#         print(a)
#         print(b)
#   for i in range(2, n):
#         c = a + b
#         a = b
#         b = c
#         print(c)


#fibonacci(-10)

data='Luthra, Shivani <shivani.a.luthra@capgemini.com>; on behalf of; IN, Architects Desk <architectsdesk.in@capgemini.com>'
tags=data.split()
print (tags)
sm_col_rem=tags[2].rstrip(';')
print (sm_col_rem)
pos1=data.find('<')
pos2=data.find('>',pos1)
email=data[pos1+1:pos2]
print (f"Email : {email}")
name=tags[1] + ' ' +tags[0].rstrip(',')
print (f"Name : {name}")
tag_rem_dl_right=tags[9].rstrip('>')
#print (tag_rem_dl_right)
tag_rem_dl_left=tags[9].lstrip('<')
#print (tag_rem_dl_left)
pos3=tag_rem_dl_right.find('<')
#print (pos3)
#pos4=tag_rem_dl_right.find('>',pos3)
#print (pos4)
DL_email=tag_rem_dl_right[pos3+1:]
print (f"DL Email ID: {DL_email}")

#list3=[89,15,90,21,9,17,8]
# value=0
# for elm in list3:
#     if value==0:
#         value=elm
#     elif elm < value:
#         value = elm
# print (value)


# def smallest():
#    value=0
#    for elm in list3:
#      if value==0:
#           value=elm
#      elif elm < value:
#           value=elm
#    return value
# print("The SMALLEST: ",smallest())

# list3.sort()
# print ("SORTED WITH SORT() :",list3)
#
# list3=[89,15,90,21,9,17,8]
# #WITHOUT USING SORT ()
# def sort_list_ascending():
#     for i in range(len(list3)):
#         for j in range(i+1, len(list3)):
#             if list3[i]>list3[j]:
#                 list3[j],list3[i]=list3[i],list3[j]
#     return list3
# print ("Ascending order sort without SORT():", sort_list_ascending())

# list3.sort(reverse=True)
# print ("SORTED WITH SORT() :", list3)
#
# def sort_list_descending():
#     for i in range(len(list3)):
#         for j in range(i+1, len(list3)):
#             if list3[j]>list3[i]:
#                 list3[j],list3[i]=list3[i],list3[j]
#     return list3
# print ("Descending order sort without SORT():", sort_list_descending())

# def highest_in_sublist():
#  list10=[[8,10,2],[6,18,24],[26,13,39],[28,14]]
#  print ("SORTED LIST - ")
#  for sublist in list10:
#     sublist.sort()
#  print (list10)
#  print ("SECOND HIGHEST IN SUBLIST - ")
#  for sublist in list10:
#     print (sublist[-2])
#
# highest_in_sublist()

# counts=dict()
# names=['csev','cwen','csev','zqian','cwen']
# for name in names:
#     if name not in counts:
#         counts[name]=1
#     else:
#         counts[name]=counts.get(name,0)+1
# print (counts)

# def fileops_write(file_name):
#     with open(file_name,"w") as file_hndl1:
#         write_content=file_hndl1.write("1. This is a test line.Line 1 \n")
#         print (type(file_hndl1))
#         return write_content
#
# fileops_write("write_test.txt")

# def fileops_read(file_name):
#     with open (file_name,"rt") as file_hndl1:
#         read_content=file_hndl1.read()
#         print (type(file_hndl1))
#         return  read_content
# print (fileops_read("write_test.txt"))

# def fileops_append(file_name):
#     with open (file_name,'a') as file_hndl1:
#         write_content=file_hndl1.write("2. This is test line. Line 2 \n")
#         return write_content
# fileops_append("write_test.txt")

# list2=[5, 10, 15, 20, 25, 30,35, 40 , 45 , 50 ]
# new_list=list2[::-1]
# print ("Reverse: ",new_list)

# def palindrom():
#  inp=input("Please enter a String value:")
#  if inp[::]==inp[::-1]:
#   print ("Palindrome!!")
#  else:
#      print ("Not a Palindrome!!")
# palindrom()

import pandas as pd
import numpy as np
import ydata_profiling as yp
def test_base():

#Setting Pandas DataFrame display options.
 pd.set_option('display.max_columns',None)
 pd.set_option('display.max_rows',100)
 # print("Display Max Rows - ",pd.get_option('display.max_rows'))
 # print ("Display Max Columns - ",pd.get_option('display.max_columns'))

# Read CSV - Create DataFrame
df_sales_data=pd.read_csv('CustomerSalesDataSet.csv')

# # DataFrame Shape
# print ("Number of Columns : ",len(df_sales_data.columns))
# print ("Number of Records  : ",df_sales_data.count())
# print ("Number of Unique Records", df_sales_data.nunique())
# print ("Top 10 rows..")
# print (df_sales_data.head(10))
# print (df_sales_data.describe())
# print ("Profit Details - ", df_sales_data["Profit"].describe())


# Dataframe Profiling
# profile=yp.ProfileReport(df_sales_data)
# profile.to_file('output.html')
# profile.to_file('output.json')

#SQL Comparision
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
# res_set5=df_sales_data[["OrderID","OrderDate","ShipDate","CustomerID","CustomerName","Address_City","Address_State","Address_Postal_Code","Product_ID"]].head(5)
# print (res_set5)
#print (type(res_set5))
#print ("SELECT DATAFRAME WITH ORDER ID AND CUSTOMERNAME")
#res_set6=df_sales_data[["OrderID","CustomerID","CustomerName"]].head(100)
#print (res_set6)
# res_set1=df_sales_data[["OrderID","CustomerID","CustomerName"]] [df_sales_data["CustomerName"]=='Muhammed Yedwab']
# print (res_set1)
#print ("With string equivalent of Like in Pandas")
# res_set2=df_sales_data[["OrderID","OrderDate","ShipDate","Category" ,"Sub_Category","CustomerID","CustomerName"]] [df_sales_data["CustomerName"].str.contains("Muh")]
# print (res_set2)
#FROM THE CITY HOUSTON
# res_set3=df_sales_data[["OrderID","OrderDate","ShipDate","Category" ,"Sub_Category","CustomerID","CustomerName","Address_City"]] [df_sales_data["Address_City"]=="Houston"]
# print (res_set3)
#res_count_city_hst=df_sales_data["Address_City"]=='Houston'
#print (type(res_count_city_hst))
#print ("No. of customers from Houston - " , res_count_city_hst.value_counts())
# temp_res=df_sales_data.head(2)
# print (temp_res)
#ADDRESS CITY = PHILADELPHIA AND SHIP MODE = FIRST CLASS FOR ONLY FIVE ROWS.
# print ("Print 5 rows for customers from the city Philadelphia.")
# res_phlildlp= df_sales_data[["OrderID","CustomerName","Address_City","ShipMode"]] [df_sales_data["Address_City"].str.contains("Phil")].head(10)
# print (res_phlildlp)

# res_phildlp_frst_cls= df_sales_data[["OrderID","CustomerName","Address_City","ShipMode"]] [(df_sales_data["Address_City"]=="Philadelphia") & (df_sales_data["ShipMode"]=="First Class")]
# res_phildlp_frst_cls_cnt= df_sales_data[(df_sales_data["Address_City"]=="Philadelphia") & (df_sales_data["ShipMode"]=="First Class")]
# print ("Total count of Philadelphia people shipping in First Class - ",len(res_phildlp_frst_cls_cnt))
# print (res_phildlp_frst_cls)
# print ("Shape of the DataFrame (ROWS)- ",res_phildlp_frst_cls_cnt.shape[0] )
# print ("Shape of the DataFrame (COLS)- ",res_phildlp_frst_cls_cnt.shape[1]  )

# res_houstn_data=df_sales_data[["OrderID","CustomerName","Address_City","ShipMode"]] [df_sales_data["Address_City"]=="Houston"]
# print ("Houston Data - ")
# print (res_houstn_data)
# print ("Houston - Corporate Data - ")
# res_houstn_corpn_data=df_sales_data[["OrderID","CustomerName","Address_City","Segment"]] [(df_sales_data["Address_City"]=="Houston") | (df_sales_data["Segment"]=="Corporate")]
# print (res_houstn_corpn_data)
# print ("Length of the data - " ,len(res_houstn_corpn_data))

#How to create a random dataframe in Python?
# randm_df=pd.DataFrame(np.random.randint(0,100,size=(100,4)), columns= list('ABCD'))
# print (randm_df)
# print ("Length of the DataFrame - ", len(randm_df))

# Check NaN
# dict_frame={"col1":["A", "B", np.NaN,"C","D"],"col2":["F",np.NaN,"G","H","I"]}
# print (type(dict_frame))
# chk_nan_frame=pd.DataFrame({"col1":["A", "B", np.NaN,"C","D"],"col2":["F",np.NaN,"G","H","I"]})
# print (type(chk_nan_frame))
# print ("DataFrame with NaN Values -")
# print (chk_nan_frame)
# print ("Only NaN Values- ")
# print (chk_nan_frame[chk_nan_frame["col2"].isna()])
# print ("Only non NaN Values- ")
# print (chk_nan_frame[chk_nan_frame["col2"].notna()])
# print ("Replace NaN with meaningful Value -")
# new_frame_A=chk_nan_frame["col1"].fillna('Not Available')
# print (new_frame_A)
# new_frame_B=chk_nan_frame["col2"].replace(np.NaN,'Not Available')
# print (new_frame_B)
# #Produce a final Frame with NaN replaced with meaningful Values
# # print ("Final Frame - ",final_frame)
# final_frame=chk_nan_frame[["col1","col2"]].fillna("Not Available")
# print (final_frame)

# JOINS
random_df_A=pd.DataFrame({"key":["A","B","C","D"],"value": np.random.randn(4)})
random_df_B=pd.DataFrame({"key":["B","D","D","E"],"value": np.random.randn(4)})
# print ("DataFrame A")
# print (random_df_A)
#
# print ("DataFrame B")
# print (random_df_B)

#select * from df1 inner join df2 on df1.key=df2.key
# print ("Inner Join -")
# inner_join_frame=pd.merge(random_df_A,random_df_B,on="key")
# inner_join_frame_2=random_df_A.merge(random_df_B,on="key")
# print (inner_join_frame)
#
# print ("Inner Join - (another way) ")
# print (inner_join_frame_2)

#LEFT OUTER JOIN
# print ("Left Outer Join -")
# left_out_join=pd.merge(random_df_A,random_df_B,on="key",how="left")
# print (left_out_join)
#
# print ("Left Outer join - Another Way ")
# left_out_join_2=random_df_A.merge(random_df_B,on="key", how="left")
# print (left_out_join_2)

#RIGHT OUTER JOIN
# print ("Right Outer Join -")
# right_out_join=pd.merge(random_df_A,random_df_B,on="key",how="right")
# print (right_out_join)
#
# print ("Right Outer Join-Another Way.")
# right_out_join_2=random_df_A.merge(random_df_B,on="key",how="right")
# print (right_out_join_2)

#FULL OUTER JOIN.
# print ("Full Outer Join -")
# full_out_join=pd.merge(random_df_A,random_df_B,on="key",how="outer")
# print (full_out_join)
#
# print ("Full Outer Join - Another way")
# full_out_join_2=random_df_A.merge(random_df_B,on="key", how="outer")
# print (full_out_join_2)

# SET_INDEX
# print ("Using SET_INDEX.")
# indexed_frame=random_df_B.set_index("key")
# print (indexed_frame)
# print (pd.merge(random_df_A,indexed_frame,left_on="key",right_index=True))
#
#
# dict_test={'Name':['Pankaj','Meghna','Lisa'],'ID1':[1,2,3],'Country':['India','India','USA'],'Role':
#            ['CEO','CTO','CTO']}
# frame_1=pd.DataFrame(dict_test)
#
# frame_2=pd.DataFrame({'ID2':[1,2,3],'Name':['Pankaj','Anupam','Amit']})
# print (frame_1.merge(frame_2))
# print (frame_1.merge(frame_2,left_on='ID1',right_on='ID2'))

# select Address_State , count(*) from tab group by   Address_State

#UNION ALL
#city_df_A=pd.DataFrame({"city":["Chicago","SanFrancisco","New York City"], "rank": range(1,4)})
#print (city_df_A)
#city_df_B=pd.DataFrame({"city":["Chicago","Boston","Los Angeles"], "rank": [1,4,5]})
#print (city_df_B)

# select city, rank from df1 union all select city , rank from df2

# print ("UNION ALL!!")
# union_all_df=pd.concat([city_df_A,city_df_B])
# print (union_all_df)

#UNION
# select city, rank from df1 union select city , rank from df2
# print ("UNION!!")
# union_df=pd.concat([city_df_A,city_df_B]).drop_duplicates()
# print (union_df)


#GROUP BY

#select Address_State , count(*) from tab group by   Address_State
# print ("GROUP BY !!")
# df_groupby=df_sales_data.groupby("Address_State").size()
# print ("Length of the dataframe - ", len(df_groupby))
# print (df_groupby)

# df_groupby_A=df_sales_data.groupby("Address_State") ["OrderID"].count()
# print ("Length of the dataframe - ", len(df_groupby_A))
# print (df_groupby_A)

#select Address_State , count(*) from tab group by   Address_State

#Difference between a group's count and size in Pandas
df = pd.DataFrame({"price":[500,300,700, 200,np.nan], "brand": ["apple", "google", "apple", "google","apple"], "device":["phone","phone","computer","phone","phone"]}, index=["a","b","c","d","e"])
#print (df)
#
# df_groupby_count=df.groupby("brand").count()
# print (type(df_groupby_count))
# print (df_groupby_count)
#The return type is a DataFrame.
#The count for apple's price is 2 since only non-nan values are counted.

# df_groupby_size=df.groupby("brand").size()
# print (type(df_groupby_size))
# print (df_groupby_size)
# the return type is Series.
# the size of brand apple is 3 since the size just counts the number of rows of each group.

#select sub_category , avg(sales) from tab group by sub_category.
#print("Average Sales!!")
#print (df_sales_data[["OrderID","OrderDate","ShipDate","CustomerID","CustomerName","Address_City","Address_State"]].head(10))
# df_average=df_sales_data.groupby("Sub_Category").agg({"Sales":np.mean})
# print (df_average)
# df_average_size=df_sales_data.groupby("Sub_Category").agg({"Sales":[np.mean,np.size]})
# print (df_average_size)

#USE PANDAS AGG METHOD ON DATAFRAME.
df=pd.DataFrame([[100,95,87],[94,92,81],[75,84,91]],columns=['Maths', 'English', 'Science'])
#print (df)

#Using over the rows.
#Total score scored by each student in all the subjects . So we can see that we need to perform an
#agg function of the sum over all the rows.
#print (df.agg(['sum'],1))

#Using over the columns.Average marks of students across all subjects.
#print (df.agg(['average'],0))

# DataFrame with the list of functions over the Rows and Columns.Instead of running this one by one we can
#pass a list of functions and it will return a DataFrame containing all the required data.

#print (df.agg(['average','min','max'],0))

#Similarly we can run this to get data for each student.
#print (df.agg(['average','min','max'],1))

#Different aggregations per column . We can run different aggregations on the column based on what
#data we require. For example , we need the average score in 'Maths' ,'Minimum' score in English and
# 'Maximum' score in Science.
# new_df=df.agg(Average_score=('Maths','average'),Minimum_score=('English','min'),Maximum_score=('Science','max'))
# print (new_df)

#How to use Pandas agg() Method in Series.
#Create a series.
score={'Harsh': 97, 'Manish': 86, 'Dev': 76}
series=pd.Series(data=score)
# print (series)
# print ("-------------------------------------")
#Running Aggregate Function on Series.
#print (series.agg({'average'}))

#How to use agg() method Per Group.
df=pd.DataFrame({'A':[1,1,2,2,3],'B':[1,2,3,4,5],'C':np.random.randn(5)})
# print (df)
# print ("-------------------------------------")
new_df=df.groupby('A').agg({'C':{'min','max'}})
#print (new_df)

if __name__=="__main__":
   test_base()

# def duplicates():
#  l1=[1,5,9,2,0,4]
#  l2=[4,8,6,0,2]
#  l3=[]
#
#  for x in range(len(l1)):
#     for y in range(len(l2)):
#         if l1[x]==l2[y]:
#             l3.append(l1[x])
#  return l3
#
# if __name__=="__main__":
#     print ("Duplicate Values: ",duplicates())


# l1=[1,5,9,2,0,4]
# l2=[4,8,6,0,2]
#
# set1=set()
# set2=set()
# set3=set()
# set4=set()
# set1=set(l1)
# print (type(set3))
# set2=set(l2)
# set3=set1.intersection(set2)
# print ("INTERSECTION - ",set3)
# set4=set1.union(set2)
# print ("UNION - ", set4)

# set5=set()
# res=[]
# set5=set2.difference(set1)
# for elm in set5:
#     res.append(elm)
# print ("DIFFERENCE - ", res)












