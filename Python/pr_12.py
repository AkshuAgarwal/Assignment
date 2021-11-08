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

Write a Python code (i) to change the Rows Label ‘Maths’ to ‘Mathematics’ and ‘Science’ to ‘SSc’, and (ii) to change
the Column Label ‘Arnab’ to ‘Aman’, and ‘Riya’ to ‘Shreya’. (iii) Print the DataFrame ResultDF
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

result_df.rename(index={"Maths": "Mathematics", "Science": "SSc"}, inplace=True)
result_df.rename(columns={"Arnab": "Aman", "Riya": "Shreya"}, inplace=True)
print(result_df)
