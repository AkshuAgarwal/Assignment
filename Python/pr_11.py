"""
Create a DataFrame ResultDF, contains

+---------+---------+---------+------------+--------+-----------+
|         |   Arnab |   Ramit |   Samridhi |   Riya |   Mallika |
|---------+---------+---------+------------+--------+-----------|
| Maths   |      90 |      92 |         89 |     81 |        94 |
| Science |      91 |      81 |         91 |     71 |        95 |
| Hindi   |      97 |      96 |         88 |     67 |        99 |
| English |      95 |      86 |         95 |     80 |        95 |
+---------+---------+---------+------------+--------+-----------+

Write a Python Program to (i) delete column ‘Ramit’ and ‘Mallika’ (ii) Delete Rows Hindi, Show the ResultDF.
"""

import pandas as pd

data = {
    "Arnab": [90, 91, 97, 95],
    "Ramit": [92, 81, 96, 86],
    "Samridhi": [89, 91, 88, 95],
    "Riya": [81, 71, 67, 80],
    "Mallika": [94, 95, 99, 95],
}
result_df = pd.DataFrame(data, ["Maths", "Science", "Hindi", "English"])
print(result_df)

del result_df["Ramit"]
del result_df["Mallika"]
result_df.drop(["Hindi"])
print(result_df)
