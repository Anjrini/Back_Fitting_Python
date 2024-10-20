# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 14:59:09 2024

@author: Mustafa anjrini
"""

import numpy as np
import pandas as pd


#creating a function that uses the back fitting method in order to get the
#coefficients of a multiple linear regression using only the implemenation
#of an iteratively linear regression of one variable

def back_fitting(response,data_frame):
    
    #a function to get the coefficients of a linear regression
    def linear_model(y,x):
        b_1=np.dot((x-np.mean(x)),(y-np.mean(y)))/np.dot((x-np.mean(x)),(x-np.mean(x)))
        b_0=np.mean(y)-b_1*np.mean(x)
        return [b_0,b_1]


    # assiging the variable y to the response
    y=response
    #assigning the variable df as a data frame
    df=data_frame
    #getting the location of the response the columns
    r=np.where(y==df.columns)[0][0]

    #if the location of the response is not in the first columns let's
    #manipulate the data frame to make it in the first column
    if r!=1:
        df=df.rename(columns={y:"y"})
        df=pd.concat([df["y"],df.iloc[:,:r],df.iloc[:,r+1:]],axis=1)
        df.columns

    #creating a vector of the cofficients with 0 values
    b=np.zeros(df.shape[1])

    #running the back fitting method using the coefficients a  single linear regression b0 and b1
    #iteratively in order to get the coefficients of our covariats
    for i in np.arange(1000):
        old_b=b[1]
        for j in np.arange(1,df.shape[1]):    
            yy=df["y"]-np.dot(df.iloc[:,1:j],b[1:j])-np.dot(df.iloc[:,j+1:],b[j+1:])      
            b[0]=linear_model(yy, df.iloc[:,j])[0]
            b[j]=linear_model(yy, df.iloc[:,j])[1]
        new_b=b[1]
        #exiting the loop if there are no more changes
        if round(new_b,6)==round(old_b,6):
            #printing the number of iterations needed
            print("\n the number of iterations needed",i*j)
            break
        elif i==999:
            #printing a message if the method did not converage
            print("\n the method did not converage")
    return b
                

####### example for 20 predictors and 1 respone #######

#setting a random rng to reproduce the data
rng=np.random.default_rng(0)

#creating a matrix containing 100 rows, 20 columns, 1 response
n=21 # number of columns
m= np.zeros((100,n))
for i in range(m.shape[1]):
    m[:,i]= rng.standard_normal(size=100)

#converting the matrix m into a data frame
df=pd.DataFrame(m)

# for changing the column names, we need to write them ourselves
a=["x"]*n

b=[]
for i in np.arange(n):
    b.append("x"+str(i))

#given that we need a dictionary for changing the names of columns
#let us create one 

c={}
for i in np.arange(n):
    c[i]=b[i]
    
#now the variable c contains all the names of the columns
#let's use the function rename in the pandas library to change the names of the columns

df=df.rename(columns=c)

#let's rename a random column as a response y

df=df.rename(columns={'x7':"y"})

#we are ready to run our implemented function "back_fitting" and get the results

back_fitting("y", df)
