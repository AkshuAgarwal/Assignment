"""
Write a program to plot a horizontal bar chart from the height of 6 students in your class.
"""

import matplotlib.pyplot as plt

y = (168, 175, 164, 158, 150, 159)
x = (1, 2, 3, 4, 5, 6)
plt.barh(x, y)
plt.show()
