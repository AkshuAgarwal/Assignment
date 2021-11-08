"""
Prof. Singh is doing some research in the field of Environment. For some plotting purposes, he has generated
some data as:

mu = 100
sigma = 15
x = mu + sigma * numpy.random.randn(10000)
y = mu + 30 * numpy.random.randn(10000)

Write a program to plot this data on a bar-stacked horizontal histogram with both x and y. 
"""

import matplotlib.pyplot as plt
import numpy as np

mu = 100
sigma = 15
x = mu + sigma * np.random.randn(10000)
y = mu + 30 * np.random.randn(10000)

plt.hist([x, y], bins=100, histtype="barstacked")
plt.show()
