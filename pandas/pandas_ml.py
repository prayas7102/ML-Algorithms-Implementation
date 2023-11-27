import pandas as pd

# series in pandas
data = pd.Series([0.24,3, 2, 432, 2])
print(data)

# series with pre defined index
data = pd.Series([0.24,3, 2, 432, 2], index=['a','b','c','d','e'])
print(data)
print(data['b'])

# series with input dict
data = {'a': 1, 'b':3}
data = pd.Series(data)
print(data)
print(data['b'])