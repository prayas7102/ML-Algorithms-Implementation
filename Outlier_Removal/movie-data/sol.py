import pandas as pd
import numpy as np
import os
import seaborn as sn
import matplotlib.pyplot as plt


def get_MAD(s, median):
    diff = abs(s - median)
    return np.median(diff)


def get_modified_z_score(x, median, MAD):
    return 0.6745 * (x - median) / MAD


# Exercise
excel_file_path = "./movie_revenues.csv"
df = pd.read_csv(excel_file_path)
# reducing revenue column of df by 1000000 times
df["revenue"] = df["revenue"] / 1000000
df = df.sort_values(by="revenue")
lower_quantile = 0.01
higher_quantile = 0.99
std_deviation = 3.5

# Calculate the 01th and 99th percentiles
per_01 = df["revenue"].quantile(lower_quantile)
per_99 = df["revenue"].quantile(higher_quantile)
per_01 -= 1.5 * (per_99 - per_01)
per_99 += 1.5 * (per_99 - per_01)

# Filter out outliers based on the percentiles
df_no_outlier = df[(df["revenue"] > per_01) & (df["revenue"] < per_99)]

# get median
median = np.median(df["revenue"])

# get MAD (median(|x-median|))
MAD = get_MAD(df["revenue"], median)

# removing outlier using zscore
df_no_outlier["modifies_z_score"] = get_modified_z_score(
    df_no_outlier["revenue"], median, MAD
)
df_no_outlier = df_no_outlier[(df_no_outlier["modifies_z_score"] < std_deviation)]

print(
    "STD before and after outlier removal",
    df["revenue"].std(),
    df_no_outlier["revenue"].std(),
)

# Specify the path where you want to save the CSV file
csv_file_path = "./output_file.csv"

# Check if the file already exists and delete it
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing file '{csv_file_path}' deleted.")
    print("\n")

# Write the DataFrame without outliers to a CSV file
df_no_outlier.to_csv(csv_file_path, index=False)

# normal distribution
# if you apply log function to a datset it becomes log normally distributed
sn.histplot(data=df_no_outlier["revenue"], kde=True, log_scale=True)
plt.show()
