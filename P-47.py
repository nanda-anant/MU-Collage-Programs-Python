
# Program to handle missing data using dropna() and fillna()

import pandas as pd
import numpy as np

# Create DataFrame with missing values
data = {
    'Name': ['Anant', 'Jeet', 'Rahul', 'Amit', 'Jay'],
    'Age': [22, np.nan, 23, 21, np.nan],
    'Marks': [85, 90, np.nan, 80, 95]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Remove rows containing missing values
print("\nDataFrame after dropna():")
print(df.dropna())

# Fill missing values with 0
print("\nDataFrame after fillna():")
print(df.fillna(0))

# Fill missing Age with average age
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("\nDataFrame after filling Age with average:")
print(df)
