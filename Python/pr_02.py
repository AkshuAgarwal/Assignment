"""
Write python code to find out the areas that are more than 50000 km^2.
The series area has been created like :-

area = pd.Series([3659,858,9659,78965,34568, 12456, 6935, 25649, 85214, 9645,3695])
"""

import pandas as pd

area = pd.Series([3659, 858, 9659, 78965, 34568, 12456, 6935, 25649, 85214, 9645, 3695])

print(*[i for i in area if i > 50000], sep="\n")
