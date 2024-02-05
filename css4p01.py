# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:42:38 2024

@author: salma
"""

"""
Extract, Load, Transform data
"""

import pandas as pd

df = pd.read_csv("movie_dataset.csv")

print(df)
print(df.info())

#change column names: remove brackets
df.rename(columns = {'Runtime (Minutes)':'Runtime_minutes',
                     'Revenue (Millions)':'Revenue_millions'
                     }, inplace= True)


"""
find and replace missing values
if integer, replace with mean
if string- remove
"""

#find which variables has missing data: use the "is.null" and "any" function to pick up any NaNs

print(df.isnull().any())

"""
Revenue millions and metascore has missing values. 
Check datatype: if int or float theb replace with mean and for string then drop missing observation
"""

print(df.info())
#variables are float therefore replace with mean

#get the mean values for revenue and metascore
print(df.describe())

"""
use fillna function to add mean scores to missing
"""

#revenue
df["Revenue_millions"] = df["Revenue_millions"].fillna(value=82.96)


#metascore
df["Metascore"] = df["Metascore"].fillna(value=58.99)



"""
Q1
"""
#use the idxmax function to determine which has highest rating
df.loc[df["Rating"].idxmax()]

"""
Q2
"""
#Used the values obtained in line 44

"""
Q3
"""

#create dataframe with just movies in years 2015-2017
list = (df.loc[df["Year"].isin([2015, 2016, 2017])])

##double check that df does not contain movies in year 2017?
print(df.loc[df["Year"] == 2017])

#check average of revenue

print(list.describe())


"""
Q4
"""
#check the counts of movies released in 2016 using value_counts function
list["Year"].value_counts()[2016]


"""
Q5
"""
#as in Q4, value_counts were used for a specific string
df["Director"].value_counts()["Christopher Nolan"]


"""
Q6
"""
#creating a new df to determine how many movies with rather higher or equal to 8
list2 = df[df["Rating"] >= 8]


"""
Q7
"""
#create a new df with only christopher nolan movies and describe to see median value of his movies
list3 = df[df["Director"] == "Christopher Nolan"]
pd.set_option('display.max_columns', None)
print(list3.describe())

"""
Q8
"""
"""
create separate df for each year 
and determine the ratings for each year

"""
#average rating of 2016
list_2016 = df[df["Year"] == 2016]
print(list_2016.describe()) #6.43

#2008
list_2008 = df[df["Year"] == 2008]
print(list_2008.describe()) #6.78

#2006
list_2006 = df[df["Year"] == 2006]
print(list_2006.describe()) #7.12

#2007
list_2007 = df[df["Year"] == 2007]
print(list_2007.describe()) #7.13

"""
Q9
"""
"""
from Q8 check number of movies in each year
do % increase calculation from values taken in Q8
"""
#2006 = 44 movies
#2016 = 297 movies

x = (297-44)/44*100
print(x)

"""
Q10
"""

"""
Create a df with just the actors
split the actor names into different columns
"""
Actorlist = df["Actors"]
Actorlist = Actorlist.str.split(",", n=6, expand = True)

"""
use counter function to determine how often actor name comes up
"""
from collections import Counter

actor_counts = Counter(Actorlist[0]) + Counter(Actorlist[1]) + Counter(Actorlist[2]) + Counter(Actorlist[3])
print(actor_counts)


"""
Q11
"""

"""
Same as Q10, however just counted the number of genres presented
"""
Genre_list = df["Genre"]
Genre_list = Genre_list.str.split(",", n=6, expand=True)

genre_counts = Counter(Genre_list[0]) + Counter(Genre_list[1]) + Counter(Genre_list[2])

print(genre_counts)             

                              
"""
Q12
"""

"""
Created new df with only numerical data
used numpy for correlation function
"""
import numpy as np

#create df with only numerical data
corr_data = df.iloc[:, 6:12]

#correlate

corr = corr_data.corr(method= 'pearson')
print(corr)
