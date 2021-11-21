"""
Write a program to create a data series and then change the indexes of the Series object in any random order.
"""

import pandas as pd

series = pd.Series(
    data=[1, 2, 3, 4, 5, 6, 7, 8], index=["A", "B", "C", "D", "E", "F", "G", "H"]
)
print(f"Data Series:\n{series}")

series_changed = series.reindex(index=["B", "G", "C", "F", "E", "A", "H", "D"])
print(f"Data Series after reindexing:\n{series_changed}")
