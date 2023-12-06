import pandas as pd
import numpy as np

# Creating a Series in pandas
data = pd.Series([0.24, 3, 2, 432, 2])
print("Series in pandas:")
print(data)
print("\n")

# Creating a series with predefined index
data = pd.Series([0.24, 3, 2, 432, 2], index=["a", "b", "c", "d", "e"])
print("Series with predefined index:")
print(data)
print("Value at index 'b':", data["b"])
print("\n")

# Creating a series with an input dictionary
data = {"a": 1, "b": 3}
data = pd.Series(data)
print("Series from input dictionary:")
print(data)
print("Value at index 'b':", data["b"])
print("Values greater than 2:")
print(data[data > 2])
print("\n")

# Combining pandas and numpy
arr = np.array([10, 2, 30, 40])
arr = pd.Series(arr)
print("Pandas and Numpy combined:")
print(arr)
arr1 = np.sqrt(arr)
print("Square root of the series:")
print(arr1)
print("\n")

# Using a numpy array as an index in a pandas series
index = np.array(["a", "b", "c"])
arr = np.array([3, 2, 2])
s = pd.Series(arr, index=index)
print("Series with numpy array as an index:")
print(s)
print("\n")

# Length, mean, min, max of the series
print("Size, mean, min, max of the series:")
print(s.size, s.mean(), s.min(), s.max())
print("\n")

# Sorting a series
print("Sorted series:")
print(s.sort_values())
print("\n")

# Unique values in a series
print("Unique values in the series:")
print(s.unique())
print("Number of unique values:")
print(s.nunique())
print("\n")

# DataFrames
df = pd.DataFrame(s)
print("DataFrame from a series:")
print(df)

name = pd.Series(["rohit", "virat"])
team = pd.Series(["MI", "RCB"])
print("\n")

# Creating a DataFrame from a dictionary
dic = {"name": name, "team": team}
df = pd.DataFrame(dic)
print("DataFrame from a dictionary:")
print(df)
print("\n")

# Creating a DataFrame from an array of dictionaries
l = [
    {"name": "ss", "sirname": "sst"},
    {"name": "1ss", "sirname": "1sst"},
    {"name": "2ss", "sirname": "2sst"},
]
df = pd.DataFrame(l)
print("DataFrame from an array of dictionaries:")
print(df)
print("\n")

# Iterating through a DataFrame
print("Iterating through a DataFrame:")
for col_index, col_name, col_sirname in df.itertuples():
    print(col_index, col_name, col_sirname)
print("\n")

# Renaming a column
df.columns = ["a", "b"]
print("Renamed DataFrame columns:")
print(df)
print("\n")

# Adding a column
list1 = [1, 2, 3, 4, 5, 6]
list2 = [11, 12, 13, 14, 15, 16]
dic = {"list1": list1, "list2": list2}
df = pd.DataFrame(dic)
df["list3"] = 20
df["list4"] = df["list3"] + df["list2"] + df["list1"]
print("DataFrame with added columns:")
print(df)

# Deleting a column
del df["list1"]
df0 = df.pop("list2")
print("DataFrame with deleted columns:")
print(df0)
print("\n")

# Deleting rows
df1 = df.drop(index=[1, 2], axis=0)
print("DataFrame with deleted rows:")
print(df1)
print("\n")

# Deleting columns
df1 = df.drop("list3", axis=1)
print("DataFrame with deleted columns:")
print(df1)
print("\n")

# Boolean indexing
df1 = pd.DataFrame(dic, index=[True, False, True, False, True, False])
print("Boolean indexing in a DataFrame:")
print(df1)
print("Row where index is False:")
print(df1.loc[False])
print("\n")

# Concatenating data frames
dic = {"list3": [45, 22, 1], "list4": [2, 3, 2]}
df1 = pd.DataFrame(dic)
df2 = pd.concat([df1, df])
print("Concatenated DataFrames:")
print(df)
print(df2)
print("\n")

# Quartiles
print("Descriptive statistics of DataFrame:")
print(df.describe())
print("\n")
print("Quartiles of 'list4' column:")
print(df.list4.quantile([0.25, 0.75]))
print("\n")

# Filling NaN values
print("Value at 'list4' index 1 before filling NaN:", df["list4"][1])
df["list4"][1] = np.NaN
print("DataFrame with NaN value:")
print(df)
print("Median of 'list4' after filling NaN:", df.list4.median())
df = df.fillna(df.list4.min())  # Filling NaN with the minimum value
print("DataFrame after filling NaN values:")
print(df)
print("\n")

# Using loc and iloc
print("Using iloc to access the first row:")
print(df.iloc[0])
print("Using loc to access the first row:")
print(df.loc[0])
print("\n")
