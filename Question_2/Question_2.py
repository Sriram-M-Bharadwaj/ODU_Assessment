#Question 2
import pandas as pd
import numpy as np
df=pd.read_csv("autos.csv",encoding='latin-1')


# a. Find Average price of autos ( using price column of dataset)

price=df.price #selecting price column
price.mean()  #calculates average of the price
#-------------------------------------------------------------------------------------------------------------------------------------

#b.Print the list of different possible types of VehicleType found in dataset

df['vehicleType'].dropna().unique() #drop null values and select unique values
#-------------------------------------------------------------------------------------------------------------------------------------

#c.	Calculate and print lowest yearOfRegistration  and highest yearOfRegistration 

yor=df['yearOfRegistration']
print(yor.min()) #find minimum  
print(yor.max()) #find maximum
#-------------------------------------------------------------------------------------------------------------------------------------

#d.	Find and print standard deviation of column kilometer

km=df['kilometer']
km.std() #standard deviation
#-------------------------------------------------------------------------------------------------------------------------------------

#e.	Draw a bar graph to represent count of different type of column brand

brand=df['brand']
x=brand.unique()  #get distinct brand values
count=[]         #declare list to hold the count values
for i in x:     #run a loop over the distinct brand values and get the count of particular brands using value_counts() and store it in count[]
    count.append(brand.value_counts()[i])
import matplotlib.pyplot as plt
plt.bar(x,count)
plt.xlabel("brands")  #define label for x & y
plt.ylabel("count")
#-------------------------------------------------------------------------------------------------------------------------------------

#f.	Find out which VehicleType  is sold minimum and maximum

vt=df['vehicleType'].dropna().unique()
count2={}
vehicletype=df['vehicleType']
for i in vt:
        count2[i]=vehicletype.value_counts()[i]
 #-------------------------------------------------------------------------------------------------------------------------------------


#g.	Create a pie chart to represent different types of  gearbox count 

count3=[]
gb=df['gearbox'].dropna().unique()  #drop null values and get distinct values of type of gearbox
for i in gb:
        count3.append(df['gearbox'].value_counts()[i]) # store the COUNT of particular type of gearbox into list count3[]

def func(pct, allvalues):                           #since autopct attribute of pie() only prints the percentage, to display the count define a function
    absolute = int(pct / 100.*np.sum(allvalues))      #that converts percentage to count value
    return "{:.1f}%\n({:d} )".format(pct, absolute)


plt.pie(count3,labels=gb, autopct = lambda pct: func(pct, count3)) # plot the pie chart. lambda used to call func()


