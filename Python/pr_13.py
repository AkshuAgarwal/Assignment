"""
Create the following DataFrame Sales containing year wise sales figures for five sales persons in INR. Use the
years as column labels, and sales person names as row labels.

+---------+--------+--------+--------+--------+
|         |   2014 |   2015 |   2016 |   2017 |
|---------+--------+--------+--------+--------|
| Madhu   |  100.5 |  12000 |  20000 |  50000 |
| Kusum   |  150.8 |  18000 |  50000 |  60000 |
| Kinshuk |  200.9 |  22000 |  70000 |  70000 |
| Ankit   |  30000 |  30000 | 100000 |  80000 |
| Shruti  |  40000 |  45000 | 125000 |  90000 |
+---------+--------+--------+--------+--------+

Write a Python Program to do the following :-
a) Display the row labels of Sales.
b) Display the column labels of Sales.
c) Display the data types of each column of Sales.
d) Display the dimensions, shape, size and value of Sales.
e) Display the last two rows of Sales.
f) Display the first two columns of Sales.
g) Check if Sales DataFrame is empty or it contains data.
"""

import pandas as pd

data = {
    2014: [100.5, 150.8, 200.9, 30000, 40000],
    2015: [12000, 18000, 22000, 30000, 45000],
    2016: [20000, 50000, 70000, 100000, 125000],
    2017: [50000, 60000, 70000, 80000, 90000],
}

sales = pd.DataFrame(data, index=["Madhu", "Kusum", "Kinshuk", "Ankit", "Shruti"])
print(sales)

# a:
print(f"Row Labels of Sales:\n{sales.index}", end="\n\n")

# b:
print(f"Column Labels of Sales:\n{sales.columns}", end="\n\n")

# c:
print(f"DTypes for each column:\n{sales.dtypes}", end="\n\n")

# d:
print(f"Shape: {sales.shape}\nSize: {sales.size}\nValues:\n{sales.values}", end="\n\n")

# e:
print(f"Last 2 rows of Sales:\n{sales.tail(2)}", end="\n\n")

# f:
print(f"First 2 columns of Sales:\n{sales.head(2)}", end="\n\n")

# g:
print(f"Is Sales empty?: {sales.empty}", end="\n\n")
