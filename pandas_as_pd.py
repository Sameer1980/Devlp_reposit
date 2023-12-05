# pandas-profiling primary goal is to provide a one-line Exploratory Data Analysis (EDA) experience in a consistent and fast solution. 
#Like pandas df.describe() function, that is so handy, pandas-profiling delivers an extended analysis of a DataFrame while alllowing the data analysis to be exported in different formats such as html and json.

# The package outputs a simple and digested analysis of a dataset, including time-series and text.
#pip install ydata-profiling
import pandas as pd
import ydata_profiling as yp
import numpy as np

pd.set_option('display.max_columns',None)
# pd.set_option('display.max_rows',100)
# print (pd.get_option('display.max_rows'))
# print (pd.get_option('display.max_columns'))
#pd.reset_option("max_columns")
#print ('Hello world!!')
df1= pd.read_csv('CustomerSalesDataSet.csv')
#print(df1.head(10))
# print (df1.describe())
# profile=yp.ProfileReport(df1)
# profile.to_file('output.html')
# profile.to_file('output.json')
#print (df1.columns)
# print ("Number of columns:", len(df1.columns))
# #print ("No. of records:",df1.count())
# print ("No.of distinct records",df1.nunique())
#unique_row_count=len(df1.drop_duplicates())
# print (unique_row_count)
#Shape of dataset
#print (unique_row_count,len(df1.columns))
#print (df1.head(5))
# print (df1.describe())

#SQL comparision
#select orderID,orderdate,shipdate,customerID,customername from tab1 limit 5

# res_set1=df1[["OrderID","OrderDate","ShipDate","CustomerID","CustomerName"]].head(5)
# print (res_set1)

# res_set2=df1[["OrderID","CustomerName"]].head(5)
# print (res_set2)

# res_set3=df1[["CustomerName"]].head(5)
# print(res_set3)

#select * from tab where address_city='Houston' / Using where clause

# res_set4=df1[df1["Address_City"]=='Houston'].head(5)
# print (res_set4)

#select "OrderID","OrderDate","ShipDate","CustomerID","CustomerName","Address_City" from 
#where address_city='Houston' limit 5

# res_set5=df1[["OrderID","OrderDate","ShipDate","CustomerID","CustomerName","Address_City"]] [df1["Address_City"]=='Houston'].head(5)
# print (res_set5)

# city=df1["Address_City"]=='Houston'
# print ("Address_city with the name Houston",city.value_counts())

#print (df1.head(5)) # Philadelphia , ShipMode=Standard Class or First Class

# select OrderID,CustomerName,Address_City,ShipMode from tab where address_city ='Philadelphia' and 
#Shipmode='First Class' limit 5

# res6=df1[(df1["Address_City"]=='Philadelphia') & (df1["ShipMode"]=='First Class')].head(5)
# print (res6)

# select * from tab where address_city ='Houston' or 
#Segment='Corporate' limit 5
# res7=df1[(df1["Address_City"]=='Houston') | (df1["Segment"]=='Corporate')].head(5)
# print (res7)

#frame=pd.DataFrame({"col1":["A","B",np.NaN,"C","D"],"col2":["F",np.NaN,"G","H","I"]})
#print (frame)

# select * from frame where col2 is null.

#print (frame[frame["col2"].isna()])

# select * from frame where col1 is not null.
#print (frame[frame["col1"].notna()])

# select Address_State , count(*) from tab group by   Address_State

#print (df1.groupby("Address_State").size())

#print (df1.groupby("Address_State")["OrderID"].count())

#select sub_category , avg(sales) from tab group by sub_category

#print (df1.groupby("Sub_Category").agg({"Sales":np.mean}))
#print (df1.groupby("Sub_Category").agg({"Sales":[np.mean,np.size]}))

df1=pd.DataFrame({"key":["A","B","C","D"],"value":np.random.randn(4)})
df2=pd.DataFrame({"key":["B","D","D","E"],"value":np.random.randn(4)})
#print (df1)

#select * from df1 inner join df2 on df1.key=df2.key
#print (pd.merge(df1,df2,on="key"))

#Set index
# indexed_df2=df2.set_index("key")
# print (pd.merge(df1,indexed_df2,left_on="key",right_index=True))

#Left outer join

#print (pd.merge(df1,df2,on="key",how="left"))

#Right outer join
#print (pd.merge(df1,df2,on="key",how="right"))

#Full outer join
#print (pd.merge(df1,df2,on="key",how="outer"))

#Union
df1=pd.DataFrame({"city":["Chicago","SanFrancisco","New York City"], "rank": range(1,4)})
#print (df1)
df2=pd.DataFrame({"city":["Chicago","Boston","Los Angeles"], "rank": [1,4,5]})
#print (df2)

# select city, rank from df1 union all select city , rank from df2
#print (pd.concat([df1,df2]))

# select city, rank from df1 union select city , rank from df2
#print (pd.concat([df1,df2]).drop_duplicates())

# Performance tuning
df1.info()
df1.info(verbose=False , memory_usage='deep')
df1.info(verbose=True , memory_usage='deep')

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import dask.dataframe as dd

df=pd.read_csv('CustomerSalesDataSet.csv')

#Convert Pandas dataframe to Pyarrow table.
table=pa.Table.from_pandas(df)

#Check for column types in Pandas.
print (df.types)

print (table)

#Write PyArrow table to Parquet file.
pq.write_table(table,'my_file.parquet')

#df.info(verbose=False,memory_usage='deep')
cols=["OrderID","OrderDate","ShipDate","Address_City","Address_State","Address_Postal_Code"]
pq_df=pd.read_parquet('my_file.parquet',engine='fastparquet',columns=cols)
pq_df.info(verbose=False,memory_usage='deep')
better_dtypes={
  "RowID": "int64",
  "OrderID": "string[pyarrow]",
  "OrderDate": "string[pyarrow]",
  "ShipDate": "string[pyarrow]",
  "ShipMode": "string[pyarrow]",
  "CustomerID" : "string[pyarrow]",
  "CustomerName" : "string[pyarrow]",
  "Segment" : "string[pyarrow]",
  "Address_Country" : "string[pyarrow]",
  "Address_City" : "string[pyarrow]",
  "Address_State": "string[pyarrow]",
  "Address_Postal_Code" : "int64",
  "Address_Region" : "string[pyarrow]",
  "Product_ID" : "string[pyarrow]",
  "Category" : "string[pyarrow]",
  "Sub_Category" : "string[pyarrow]",
  "Sales" : "float64",
  "Quantity" : "int64",
  "Discount" : "float64",
  "Profit" : "float64",
  }
#Using normal dataframe with groupby.
df2=pd.read_csv('CustomerSalesDataSet.csv')
df2.groupby("Product_ID",dropna=False,observed=True).agg({"Sales": "sum"})
df2.info(verbose=False,memory_usage='deep')
#Using Dask dataframe with groupby.
ddf=dd.read_csv("CustomerSalesDataSet.csv", dtype=better_dtypes)
ddf.groupby("Product_ID",dropna=False,observed=True).agg({"Sales": "sum"})).compute()
ddf.info(verbose=False,memory_usage='deep')




# complx_dict={}
# complx_dict={"Name":"Samir","Age":42,"Salary":80000,"details":{"ConsumerID":"CON_92475_T","InsuranceID":"XXXXXXX12569","Premium":10000,"ROI":8.2}}
# print ("Dictionary:")
# print ('---------------------------')
# for val in complx_dict.items():
#     print (val)
# print ("Keys:")
# print ('---------------------------')
# for k in complx_dict.keys():
#     print (k)

# print ("Values")
# print ('---------------------------')
# for val in complx_dict.values():
#     print (val)



