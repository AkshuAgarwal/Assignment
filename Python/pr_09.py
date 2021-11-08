"""
Write a program to iterate over a DataFrame containing names and marks, which then calculate marks as per
the criteria and then adds them to the grade column.

Marks >= 80 grade is A, Marks >= 60 grade is B, Marks < 60 grade is C 
"""

import pandas as pd
import numpy as np

names = pd.Series(["Rohan", "Samay", "Shantanu", "Shruti", "Tanya"])
marks = pd.Series([89, 76, 43, 38, 98])
stu = {"Name": names, "Marks": marks}

dfl = pd.DataFrame(stu, columns=["Name", "Marks"])
dfl["Grade"] = np.nan

print(f"Initial Values:\n{dfl}")

lstmarks = []
for col, col_series in filter(lambda column: column[0] == "Marks", dfl.iteritems()):
    for row, mks in enumerate(col_series):
        if mks >= 80:
            lstmarks.append("A")
        elif 80 > mks >= 60:
            lstmarks.append("B")
        elif mks < 60:
            lstmarks.append("C")

dfl["Grade"] = lstmarks
print(f"DataFrame after calculating Grades:\n{dfl}")
