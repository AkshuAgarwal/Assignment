"""
Write a Python program to create a Series object with 6 random integers and
having vowel characters as indexes.
"""

import pandas as pd
import numpy as np

vals = np.random.randint(0, 100, 6)
series = pd.Series(vals, index=["A", "B", "C", "D", "E", "F"])

print(series)
