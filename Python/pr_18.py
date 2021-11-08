"""
Write a program to plot a line chart to display the changing weekly onion prices for four weeks.
"""

import matplotlib.pyplot as plt

week = [1, 2, 3, 4]
prices = [48, 60, 45, 85]

plt.plot(week, prices)
plt.xlabel("Week")
plt.ylabel("Onion Prices")
plt.show()
