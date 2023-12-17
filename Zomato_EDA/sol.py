import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt

excel_file_path = "./zomato.csv"
df = pd.read_csv(excel_file_path, encoding="latin-1")
df.head()
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum()["Cuisines"])
print(df.isnull().sum()>0)
feat_with_null_val = [feat for feat in df.columns if df.isnull().sum()[feat]>0]
print(feat_with_null_val)