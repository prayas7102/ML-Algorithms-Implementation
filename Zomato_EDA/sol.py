import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline

excel_file_path = "./zomato.csv"
df = pd.read_csv(excel_file_path, encoding="latin-1")
# print(df.head())
# print(df.columns)
# print(df.info())
# finding null values in dataframe
# print(df.isnull())
# print(df.isnull().sum())
# print(df.isnull().sum()["Cuisines"])
# print(df.isnull().sum() > 0)
# print(df.dtypes)
# sns.heatmap(df.isnull())
# plt.show()
feat_with_null_val = [feat for feat in df.columns if df.isnull()[feat].sum() > 0]
# print(feat_with_null_val)
df_country = pd.read_excel("./Country-Code.xlsx")
# print(df_country.head())

df_merged = pd.merge(df, df_country, on="Country Code", how="left")
# print(df_merged.head())
# print(df_merged.Country.value_counts())

# total no. of occurances ofcountry
country_val = df_merged.Country.value_counts()
# print(country_val)
# print(country_val.values)
# print(country_val.index)
# plt.pie(country_val[:3], labels=country_name[:3], autopct="%.2f%%")
# plt.show()

# tottal count for each rating number
# After grouping, .size() counts the number of rows within each group.
# This means for each unique combination of Aggregate rating,
# Rating color, and Rating text
ratings = (
    df_merged.groupby(["Aggregate rating", "Rating color", "Rating text"])
    .size()
    .reset_index()
    .rename(columns={0: "Rating Count"})
)
# print(ratings.head())
# sns.barplot(data=ratings, x="Aggregate rating", y="Rating Count", hue="Rating color")
# plt.show()

# countries where rating color is white or has given zero ratings
# reset_index to Converting Grouped Data to DataFrame:
zero_rating = (
    df_merged[df_merged["Rating color"] == "White"]
    .groupby("Country")
    .size()
    .reset_index()
    .rename(columns={0: "zero count"})
)
# print(zero_rating)

# currency for each country
currency = (
    df_merged.groupby(["Country", "Currency"])
    .size()
    .reset_index()
    .rename(columns={0: "currency occurences in table"})
)
# print(currency.head())

# countries with/without online delivery option
delivery_option_yes_no = (
    df_merged.groupby(["Country", "Has Online delivery"])
    .size()
    .reset_index()
    .rename(columns={0: "delivery_option_yes_no occurences in table"})
)
# print(delivery_option_yes_no.head())

# countries with online delivery option
delivery_option_yes = (
    df_merged[df_merged["Has Online delivery"] != "No"]
    .groupby("Country")
    .size()
    .reset_index()
    .rename(columns={0: "Online delivery count"})
)
# print(delivery_option_yes.head())

# top 10 cuisines
cuisine_val = df_merged.Cuisines.value_counts()
x = (cuisine_val.sort_values(ascending=False))
print(x[:10])
