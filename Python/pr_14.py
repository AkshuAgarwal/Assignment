"""
Write a program to read from a CSV file Employee.csv and create a DataFrame from it, and (i) Print the
DataFrame , (ii) Print the first 2 rows , (iii) Print the last 2 records.
Employee CSV files contains (Empno, Name, Desgination, Salary) of 6 employees
"""

import pandas as pd

df = pd.read_csv("./employees.csv")
print(df)

print(f"\nFirst 2 rows:\n{df.head(2)}")
print(f"\nLast 2 rows:\n{df.tail(2)}")
