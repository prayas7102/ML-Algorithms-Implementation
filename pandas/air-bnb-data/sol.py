import pandas as pd
import os
import seaborn as sn
import matplotlib.pyplot as plt

# Exercise
excel_file_path = "./archive/AB_NYC_2019.csv"
df = pd.read_csv(excel_file_path)

# Display the 'price' column
print("Original 'price' column:")
print(df.price)
print("\n")

# Display the 25th and 75th percentiles of the 'price' column
print("25th and 75th percentiles of 'price' column:")
print(df.price.quantile([0.25, 0.75]))
print("\n")

# Display descriptive statistics of the 'price' column
print("Descriptive statistics of 'price' column:")
print(df.price.describe())
print("\n")

# Calculate the 25th and 75th percentiles
per_25 = df.price.quantile(0.25)
per_75 = df.price.quantile(0.75)

# Filter out outliers based on the percentiles
df_no_outlier = df[(df.price > per_25) & (df.price < per_75)]

# Specify the path where you want to save the CSV file
csv_file_path = "./archive/output_file.csv"

# Check if the file already exists and delete it
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing file '{csv_file_path}' deleted.")
    print("\n")

# Write the DataFrame without outliers to a CSV file
df_no_outlier.to_csv(csv_file_path, index=False)

df_no_outlier["zscore"] = (
    df_no_outlier["price"] - df_no_outlier["price"].mean()
) / df_no_outlier["price"].std()

# removing outlier using zscore
df_no_outlier = df_no_outlier[
    (df_no_outlier["zscore"] > -2) & (df_no_outlier["zscore"] < 2)
]

# normal distribution
sn.histplot(data=df_no_outlier["price"], kde=True)
plt.show()

# Display lengths of the original and filtered DataFrames
print(
    f"Original DataFrame length: {len(df)}, Filtered DataFrame length: {len(df_no_outlier)}"
)
print("\n")

# Display standard deviations of the 'price' column in both DataFrames
print(
    f"Standard deviation of 'price' column in the original DataFrame: {df['price'].std()}"
)
print(
    f"Standard deviation of 'price' column in the filtered DataFrame: {df_no_outlier['price'].std()}"
)
print("\n")

# Display descriptive statistics of the 'price' column in the filtered DataFrame
print("Descriptive statistics of 'price' column in the filtered DataFrame:")
print(df_no_outlier.price.describe())
print("\n")
