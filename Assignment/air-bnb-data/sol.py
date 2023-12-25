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

lower_quantile = 0.01
higher_quantile = 0.99
zscore_std_deviation = 3

# Display the 01th and 99th percentiles of the 'price' column
print("01th and 99th percentiles of 'price' column:")
print(df.price.quantile([lower_quantile, higher_quantile]))
print("\n")

# Apply log with base 10 to the 'price' column
# df['price'] = df['price'].apply(np.log10)

# Display descriptive statistics of the 'price' column
print("Descriptive statistics of 'price' column:")
print(df.price.describe())
print("\n")

# Calculate the 25th and 75th percentiles
per_25 = df.price.quantile(lower_quantile)
per_75 = df.price.quantile(higher_quantile)
per_25 -= 1.5 * (per_75 - per_25)
per_75 += 1.5 * (per_75 - per_25)

# Filter out outliers based on the percentiles
df_no_outlier = df[(df.price > per_25) & (df.price < per_75)]

df_no_outlier["zscore"] = (
    df_no_outlier["price"] - df_no_outlier["price"].mean()
) / df_no_outlier["price"].std()

# removing outlier using zscore
df_no_outlier = df_no_outlier[
    (df_no_outlier["zscore"] > -zscore_std_deviation)
    & (df_no_outlier["zscore"] < zscore_std_deviation)
]

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

# Specify the path where you want to save the CSV file
csv_file_path = "./archive/output_file.csv"

# Check if the file already exists and delete it
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
    print(f"Existing file '{csv_file_path}' deleted.")
    print("\n")

# Write the DataFrame without outliers to a CSV file
df_no_outlier.to_csv(csv_file_path, index=False)

# normal distribution
# kde = kernel density estimator
sn.histplot(data=df_no_outlier["price"], kde=True, log_scale=True)
plt.show()
