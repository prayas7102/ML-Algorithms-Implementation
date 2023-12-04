import pandas as pd
import numpy as np

# series in pandas
data = pd.Series([0.24, 3, 2, 432, 2])
print(data)
print("\n")

# series with pre defined index
data = pd.Series([0.24, 3, 2, 432, 2], index=["a", "b", "c", "d", "e"])
print(data)
print(data["b"])
print("\n")

# series with input dict
data = {"a": 1, "b": 3}
data = pd.Series(data)
print(data)
print(data["b"])
print(data[data > 2])
print("\n")

# pandas and numpy combined
arr = np.array([10, 2, 30, 40])
arr = pd.Series(arr)
print(arr)
arr1 = np.sqrt(arr)
print(arr1)
print("\n")

# numpy array as index in pandas series
index = np.array(["a", "b", "c"])
arr = np.array([3, 2, 2])
s = pd.Series(arr, index=index)
print(s)
print("\n")

# len, mean, min, max of series
print(s.size, s.mean(), s.min(), s.max())
print("\n")

# sort a series
print(s.sort_values())
print("\n")

# unique value in series
print(s.unique())
print(s.nunique())
print("\n")

# dataframes
df = pd.DataFrame(s)
print(df)
name = pd.Series(["rohit", "virat"])
team = pd.Series(["MI", "RCB"])
print("\n")

# dict to dataframe
dic = {"name": name, "team": team}
df = pd.DataFrame(dic)
print(df)
print("\n")

# array of dict
l = [
    {"name": "ss", "sirname": "sst"},
    {"name": "1ss", "sirname": "1sst"},
    {"name": "2ss", "sirname": "2sst"},
]
df = pd.DataFrame(l)
print(df)
print("\n")

# iterating dataframe
for col_index, col_name, col_sirname in df.itertuples():
    print(col_index, col_name, col_sirname)
print("\n")

# rename column
df.columns = ["a", "b"]
print(df)
print("\n")

# add column
list1 = [1, 2, 3, 4, 5, 6]
list2 = [11, 12, 13, 14, 15, 16]
dic = {"list1": list1, "list2": list2}
df = pd.DataFrame(dic)
df["list3"] = 20
df["list4"] = df["list3"] + df["list2"] + df["list1"]
print(df)

# delete column
del df["list1"]
df0 = df.pop("list2")
print(df0)
print("\n")

# delete row wise
df1 = df.drop(index=[1, 2], axis=0)
print(df1)
print("\n")

# delete column wise
df1 = df.drop("list3", axis=1)
print(df1)
print("\n")

# bool indexing
df1 = pd.DataFrame(dic, index=[True, False, True, False, True, False])
print(df1)
print(df1.loc[False])
print("\n")

# concatnating data frames
dic = {"list3": [45, 22, 1], "list4": [2, 3, 2]}
df1 = pd.DataFrame(dic)
df2 = pd.concat([df1, df])
print(df)
print(df2)
print("\n")

# quartile
print(df.describe())
print("\n")
print(df.list4.quantile([0.25, 0.75]))
print("\n")

# fill na
print(df["list4"][1])
df["list4"][1] = np.NaN
print(df)
print(df.list4.median())
df = df.fillna(df.list4.min())  # median, mean etc.
print(df)
print("\n")

# loc, iloc
print(df.iloc[0])
print(df.loc[0])
print("\n")
