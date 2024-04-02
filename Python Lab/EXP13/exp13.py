# -*- coding: utf-8 -*-
"""EXP13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iSdC5wBR4clkJRUa4nO-h366q5YWIakM

#EXPERIMENT 13

---

Importing Required Libraries
"""

import matplotlib.pyplot as plt
import math
import numpy as np

"""##Line Graphs

Line Graph of Years from 2000 to 2012 vs tables of 2 and 3
"""

#X-axis data
years = range(2000,2012)

#Y-axis data
a = [2,4,6,8,10,12,14,16,18,20,22,24]
b = [3,6,9,12,15,18,21,24,27,30,33,36]

#Ploting the line graphs
plt.plot(years,a)
plt.plot(years,b)

#Adding Labels,Legend and Titles
plt.xlabel("X-axis values (Years)")
plt.ylabel("Table of 2 and 3")
plt.title("2-input graph")
plt.legend(["T2","T3"],loc = "upper right")
plt.show()

"""Line Graph of Number vs Squareroot"""

#Declearing List
number= []
squareroot= []

#Appending Data to the Lists
for i in range(10,101,10):
  number.append(i)

for i in number:
  squareroot.append(math.sqrt(i))

#Ploting Data
plt.plot(number,squareroot)

#Adding Labels and Titles
plt.xlabel("Number")
plt.ylabel("Square Root")
plt.title("Number Vs SquareRoot Plot")
plt.show()

"""##Histogram"""

#Generating Random Data
data = np.random.randn(1000)

#Ploting Histogram
plt.hist(data, bins=10, color = "teal", edgecolor="black")

#Adding Labels and Titles
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Basic Histogram")

plt.show()

#Generating Random Data
data1 = np.random.randn(1000)
data1 = np.random.randn(1000)

#Ploting Histogram
plt.hist(data1, bins=20, color = "blue", edgecolor="black")
plt.hist(data, bins=20, color = "teal", edgecolor="black")

#Adding Labels and Titles
plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram")

plt.show()

"""##Pie Charts"""

cars = ["AUDI","BMW","FORD","TESLA", "JAGUAR", "MERCEDES"]
data = [23,17,15,27,34,50]

fig = plt.figure(figsize=(5,7))
plt.pie(data , shadow = True)
plt.legend(cars,loc = "upper right")
plt.show()

cars = ["AUDI","BMW","FORD","TESLA", "JAGUAR", "MERCEDES"]
data = [23,17,15,27,34,50]
explodes = [0.1,0.1,0.1,0.1,0.1,0.4]
fig = plt.figure(figsize=(5,7))
plt.pie(data , shadow = True, explode = explodes)
plt.legend(cars,loc = "upper right")
plt.show()

"""#POST-EXPERIMENT EXERCISE

**1. Write a Python program to create Data Frame using Dictionary, List of Tuples.**
"""

import pandas as pd

# Using dictionary
data_dict = {
    'Name': ['Vishal', 'Joseph', 'Kevin', 'Ajay'],
    'Address': ['Jalgoan', 'Ram Mandir', 'Malad', 'Borivali'],
    'Rollno': [63, 57, 5, 4],
}

df_dict = pd.DataFrame(data_dict)
print("DataFrame using Dictionary:")
print(df_dict)

# Using list of tuples
data_list = [
    ('Vishal','Jalgoan', 63),
    ('Joseph', 'Ram Mandir',57),
    ('Kevin', 'Malad',5),
    ('Ajay', 'Borivali',4)
]

df_list = pd.DataFrame(data_list, columns=['Name','Address' ,'Rollno'])
print("\nDataFrame using List of Tuples:")
print(df_list)

"""**2.Write a Python program to implement any 5 operations on Data Frame.**"""

import pandas as pd

# Creating a DataFrame
data = {
    'Name': ['Vishal', 'Joseph', 'Kevin', 'Ajay'],
    'Address': ['Jalgoan', 'Ram Mandir', 'Malad', 'Borivali'],
    'Rollno': [63, 57, 5, 4],
    'Marks':[90,65,95,75]
}

df = pd.DataFrame(data)
print("\nOriginal DataFrame:")
print(df)

# Accessing and displaying data
print("\nAccessing and displaying data:")
print("First row:")
print(df.iloc[0])
print("\nLast 2 rows:")
print(df.tail(2))
print("\nMarks column:")
print(df['Marks'])

# Adding a new column
df['PID'] = [221068, 221062, 221075, 221074]
print("\nDataFrame after adding PID column:")
print(df)

# Filtering data
filtered_df = df[df['Marks'] > 70]
print("\nFiltered DataFrame where  Marks > 70:")
print(filtered_df)

# Sorting data
sorted_df = df.sort_values(by='PID', ascending=False)
print("\nSorted DataFrame by PID:")
print(sorted_df)