import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# %matplotlib inline

excel_file_path = "./black_friday/train.csv"
df = pd.read_csv(excel_file_path, encoding="latin-1")
