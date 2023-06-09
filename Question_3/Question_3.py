# QUESTION_3

import pandas as pd
df=pd.read_csv("autos.csv",encoding='latin-1')

# 1. exploratory data analysis

df.describe()   #describe() used to apply basic statistical computations to find extreme values,count,standard deviation etc. 
df.info()       #check null values and missing data
df.isnull().sum() #checks total number of null values in column


""""Since vehicle type, model and notRepairedDamage are important features in in prediciting the price of the car they 
cannot be dropped. Hence the missing values have to be filled using some method.
The percentage of missing values is less than 70%, so they cannot be dropped."""

"""#3 The challenge faced is to fill the missing
      Data with appropriate and accurate values """

"""#4. Linear regression will be a suitable model
       for predicting the price of the cars """



