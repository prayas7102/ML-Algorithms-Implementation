import pandas as pd
import os

# Exercise
excel_file_path = "./archive/AB_NYC_2019.csv"
df = pd.read_csv(excel_file_path)
print(df.price)
print("\n")
print(df.price.quantile([0.25, 0.75]))
print("\n")
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
# Write the DataFrame to a CSV file
df_no_outlier.to_csv(csv_file_path, index=False)
print(len(df), len(df_no_outlier))
print("\n")
print(df["price"].std(), df_no_outlier["price"].std())
print("\n")
print(df_no_outlier.price.describe())
print("\n")
