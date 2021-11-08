"""
Write python code to find out the biggest and smallest three items from the given Series.
The series area has been created like :-

area = pd.Series([3659,858,9659,78965,34568, 12456, 6935, 25649, 85214, 9645,3695])
"""

import pandas as pd

area = pd.Series([3659, 858, 9659, 78965, 34568, 12456, 6935, 25649, 85214, 9645, 3695])

print(f"Biggest 3 Items:\n{area.sort_values().tail(3)}")
print(f"Smallest 3 Items:\n{area.sort_values().head(3)}")
