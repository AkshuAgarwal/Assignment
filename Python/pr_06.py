"""
Write a Python program to create a Dataframe Score containing following data :–

+---------+---------+---------+------------+--------+-----------+----------+
|         |   Arnab |   Ramit |   Samridhi |   Riya |   Mallika |   Preeti |
|---------+---------+---------+------------+--------+-----------+----------|
| Maths   |      90 |      92 |         89 |     81 |        94 |       89 |
| Science |      91 |      81 |         91 |     71 |        95 |       78 |
| Hindi   |      97 |      96 |         88 |     67 |        99 |       76 |
+---------+---------+---------+------------+--------+-----------+----------+
"""

import pandas as pd

data = {
    "Arnab": [90, 91, 97],
    "Ramit": [92, 81, 96],
    "Samridhi": [89, 91, 88],
    "Riya": [81, 71, 67],
    "Mallika": [94, 95, 99],
    "Preeti": [89, 78, 76],
}

score = pd.DataFrame(data, ["Maths", "Science", "Hindi"])
print(score)
