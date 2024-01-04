#DESCRIPTIVE ANALYTICS

import pandas as pd# Data Wrangling
import numpy as np# Numpy array
import matplotlib.pyplot as plt # Visualization
import seaborn as sns # Visualization
import ydata_profiling # Descriptive Analytics
import warnings
warnings.filterwarnings('ignore')

pd.set_option('display.float_format', lambda x: '%.3f' %x)

#Loading dataset onto dataframe
ipl_auction_df=pd.read_csv('IPL IMB381IPL2013.csv')
#print (type(ipl_auction_df))

#Displaying first few records of dataframe
pd.set_option('display.max_columns',7)
#print (ipl_auction_df.head(5))

#Finding metadata of the dataframe
#print (list(ipl_auction_df.columns))
# print (ipl_auction_df.columns)
#print (ipl_auction_df.head(5).transpose)
#print (ipl_auction_df.shape)

#Finding summary of the dataframe.
#print (ipl_auction_df.info())

#Slicing and indexing a dataframe.
# print (ipl_auction_df[0:5])
# print (ipl_auction_df[-5:])

#Selecting columns by column names.
#print (ipl_auction_df['PLAYER NAME'] [0:5])
#print (ipl_auction_df[['PLAYER NAME','COUNTRY']] [0:5])

#Select rows and columns by indexes.
#print (ipl_auction_df.iloc[4:9,1:4])

#Finding unique occurences of values in columns.
#print (ipl_auction_df.COUNTRY.value_counts())
#print (ipl_auction_df.COUNTRY.value_counts(normalize=True)*100) 

#Crosstab
#print (pd.crosstab(ipl_auction_df['AGE'],ipl_auction_df['PLAYING ROLE']))

#Sorting dataframe by column values.
#print (ipl_auction_df[['PLAYER NAME','SOLD PRICE']].sort_values('SOLD PRICE')[0:5])

#print (ipl_auction_df[['PLAYER NAME','SOLD PRICE']].sort_values('SOLD PRICE',ascending=False)[0:5])

#Creating new columns.Which player got the maximum premium on the base price?
# ipl_auction_df['premium']=ipl_auction_df['SOLD PRICE'] - ipl_auction_df['BASE PRICE']
# print(ipl_auction_df[['PLAYER NAME','BASE PRICE','SOLD PRICE','premium']][0:5])
# print(ipl_auction_df[['PLAYER NAME','BASE PRICE','SOLD PRICE','premium']].sort_values('premium',ascending=False)[0:5])

#Grouping and Aggregating
# What is the average SOLD PRICE for each age category?

# average=ipl_auction_df.groupby('AGE')['SOLD PRICE'].mean() 
# print (average)

soldprice_by_age=ipl_auction_df.groupby('AGE')['SOLD PRICE'].mean().reset_index()
# print (soldprice_by_age)

#Average SOLD PRICE for different playing roles in each age category.
soldprice_by_age_role=ipl_auction_df.groupby(['AGE','PLAYING ROLE'])['SOLD PRICE'].mean().reset_index()
# print (soldprice_by_age_role)

#Joining dataframes. Compare the average auction price for different ages and playing roles.
soldprice_comparison= soldprice_by_age_role.merge(soldprice_by_age, on='AGE',how='outer')
#print (soldprice_comparison)
#Rename columns
soldprice_comparison.rename(columns={'SOLD PRICE_x':'SOLD_PRICE_AGE_ROLE','SOLD PRICE_y':'SOLD_PRICE_AGE'},inplace=True)
#print (soldprice_comparison.head(5))

#Applying Operations to multiple columns.Percentage change in sold price.
soldprice_comparison['change']=soldprice_comparison.apply(lambda rec:(rec.SOLD_PRICE_AGE_ROLE - rec.SOLD_PRICE_AGE) / rec.SOLD_PRICE_AGE , axis=1)
#print (soldprice_comparison['change'])

#Applying Lambda function to dataframe

#Creating and initializing a list
values=[['Rohan',455],['Elvish',250],['Deepak', 495],['Soni', 400],['Radhika', 350],['Vansh',450]]

#Creating a Pandas dataframe
df=pd.DataFrame(values,columns=['Name', 'Total_marks'])

#print (df)

#Applying Lambda function to find percentage of 'Total_Marks' column.
# Using df.assign()

df = df.assign(Percentage= lambda x: (x['Total_marks']/ 500 *100))
df['Percentage'] = df.apply(lambda x: (x['Total_marks']/ 500 *100),axis=1)

#print (df.sort_values('Percentage',ascending=False))

# Filtering Records from Dataframe based on conditions.

# Which players have hit more than 80 sixes in the IPL tournament so far?

#print (ipl_auction_df.columns)
sixer_df= ipl_auction_df[ipl_auction_df['SIXERS']>80] [['PLAYER NAME','SIXERS']]
# print (sixer_df.sort_values('SIXERS',ascending=False))
# print (type(sixer_df))

#Removing a column.
# ipl_auction_df.drop('Sl.NO.', inplace=True,axis=1)
# print (ipl_auction_df.columns)

#Dealing With Missing Values.
autos=pd.read_csv('auto-mpg.data',sep='\s+', header=None)
#print (autos.head(5))

autos.columns=['mpg','cylinders','displacement','horsepower','weight','acceleration', 'year', 'origin', 'name']
#print (autos.head(5))

#autos.info()

autos["horsepower"]=pd.to_numeric(autos['horsepower'],errors='coerce')
#autos.info()

#print (autos[autos.horsepower.isnull()])

autos=autos.dropna(subset=['horsepower'])

#print (autos[autos.horsepower.isnull()])

#Exploration using Visualization Plots

#Drawing plots
# install Python Extension Pack, it includes Jupyter extension, put your code in the editor, put #%% at the top of your code, you'll get Run cell clickable,
# click it, and you'll get result in the other window
#%%
import pandas as pd# Data Wrangling
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sn


import warnings
warnings.filterwarnings('ignore')

#Bar Plot
ipl_auction_df=pd.read_csv('IPL IMB381IPL2013.csv')
soldprice_by_age_role=ipl_auction_df.groupby(['AGE','PLAYING ROLE'])['SOLD PRICE'].mean().reset_index()
soldprice_comparison= soldprice_by_age_role.merge(soldprice_by_age, on='AGE',how='outer')
soldprice_by_age=ipl_auction_df.groupby('AGE')['SOLD PRICE'].mean().reset_index()
#sn.barplot(x='AGE', y='SOLD PRICE', data=soldprice_by_age)
sn.barplot(x='AGE',y='soldprice_by_age_role', hue='PLAYING ROLE',data=soldprice_comparison)












# %%
