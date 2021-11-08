"""
Create a series object marks, containing marks of 6 students. Write a Python program to sort the values of a
Series object marks in ascending order and descending order and store it into Series object ascMarks and
descMarks respectively.
"""

import pandas as pd

marks = pd.Series(
    [98, 49, 86, 78, 96, 59], ["Ahana", "Sarthak", "Rashi", "Muskan", "Manvi", "Kashvi"]
)
print(f"Marks:\n{marks}")

asc_marks = marks.sort_values(ascending=True)
print(f"Marks after sorting in Ascending order:\n{asc_marks}")

desc_marks = marks.sort_values(ascending=False)
print(f"Marks after sorting in Descending order:\n{desc_marks}")
