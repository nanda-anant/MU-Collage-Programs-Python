
# Program to perform basic data analysis using Pandas DataFrame

import pandas as pd

# Create a dictionary of student data
data = {
    'Name': ['Anant', 'Jeet', 'Rahul', 'Amit', 'Jay'],
    'Age': [22, 21, 23, 22, 20],
    'Marks': [85, 90, 75, 80, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display complete DataFrame
print("Student Data:")
print(df)

# Display first 3 records
print("\nFirst 3 Records:")
print(df.head(3))

# Display basic information
print("\nDataFrame Information:")
print(df.info())

# Display statistical summary
print("\nStatistical Summary:")
print(df.describe())

# Calculate average marks
print("\nAverage Marks:")
print(df['Marks'].mean())

# Find maximum marks
print("\nMaximum Marks:")
print(df['Marks'].max())

# Find minimum marks
print("\nMinimum Marks:")
print(df['Marks'].min())

# Sort students by marks
print("\nStudents Sorted by Marks:")
print(df.sort_values(by='Marks', ascending=False))
