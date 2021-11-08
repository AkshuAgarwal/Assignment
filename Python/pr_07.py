"""
Write a Python program to Add one Column and one Row in the DataFrame Score, given in q.no 6.
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

score.at["English", :] = [89, 78, 64, 48, 58, 68]
score.at[:, "Priya"] = [44, 76, 68, 82]
print(score)
