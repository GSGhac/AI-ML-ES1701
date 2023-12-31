# -*- coding: utf-8 -*-
"""Copy of AI ML CSE 2nd year BTech Lab

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17Hen5nM5GM20mubPUaseJixqnXfxxHO5
"""

#write the pandas program to read csv file and print the top 5 rows

import pandas as pd

file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

print(data.head())

#Write a program to select a series from the dataset and read the content of the series.

import pandas as pd

file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

print(data.iloc[63])

# Program to rename x column to length and y column to width.

import pandas as pd

file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

data.rename(columns={'x':'length','y':'width'}, inplace = True)

print(data)

# Program to sort the cut column in ascending order and return it in a series

import pandas as pd

file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

sorted_cut_series = data['cut'].sort_values()

print(sorted_cut_series)

# Program to find diamonds that are fair or good or premium

import pandas as pd

file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

filtered_diamonds = data[data['cut'].isin(['Fair','Good','Premium'])]

print(filtered_diamonds)

# Program to calculate count, maximum and minimum price for each 'cut' of the diamonds dataframe.

import pandas as pd

file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

result = data.groupby('cut')['price'].agg(['count','min','max'])

print(result)

# Program to create a bar plot of the 'value_counts' for the 'cut' series of diamonds Dataframe

import pandas as pd
import matplotlib.pyplot as plt


file_path = '/content/drive/MyDrive/Colab Notebooks/diamonds.csv'

data = pd.read_csv(file_path)

cut_counts = data['cut'].value_counts()
cut_counts.plot(kind = 'bar', color = 'blue')

plt.xlabel('Cut')
plt.ylabel('Count')
plt.title('Distribution of Diamonds cut')

plt.show()

# Program to print a concise summary of DiamondsDataframe

import pandas as pd

file_path = "/content/drive/MyDrive/Colab Notebooks/diamonds.csv"

data = pd.read_csv(file_path)

data.info()