
# Program to create a DataFrame from CSV or Excel files

import pandas as pd

# Read CSV file
df_csv = pd.read_csv("student.csv")

print("DataFrame from CSV File:")
print(df_csv)

# Read Excel file
df_excel = pd.read_excel("student.xlsx")

print("\nDataFrame from Excel File:")
print(df_excel)
