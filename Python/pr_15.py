"""
Write a program to read from a CSV file employees.csv and create a DataFrame from it but dataframe should not
use file’s column header rather should use one column heading EmpId, EmpName, Desg, EmpSal. Also print the
maximum salary given to an employee.
Employee CSV files contains (Empno, Name, Desgination, Salary) of 6 employees.
"""

import pandas as pd

df = pd.read_csv(
    "./employees.csv", header=0, names=["EmpId", "EmpName", "Desg", "EmpSal"]
)
print(df)
print(f"Maximum Salary: {df.loc[:, 'EmpSal'].max()}")
