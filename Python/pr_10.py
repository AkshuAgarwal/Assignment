"""
Create a Dataframe Forest 'dFrameForest'

+----+---------+-------------+-------------------+
|    | State   |   GrossArea | DenseForestArea   |
|----+---------+-------------+-------------------|
|  0 | Assam   |       78438 | 2797.00           |
|  1 | Delhi   |        1483 | 6.72              |
|  2 | Kerela  |       38852 | 1663.00           |
+----+---------+-------------+-------------------+

Write a Python Program to print only the State and DenseForestArea for all rows.
"""

import pandas as pd

data = {
    "State": ["Assam", "Delhi", "Kerela"],
    "GrossArea": [78438, 1483, 38852],
    "DenseForestArea": [2792.00, 6.72, 1663.00],
}

df = pd.DataFrame(data)
print(df.loc[0:2, ["State", "DenseForestArea"]])
