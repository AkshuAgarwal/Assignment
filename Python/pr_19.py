"""
First 10 terms of a Fibonacci series are stored in a list namely

fib = [0,1,1,2,3,5,8,13,21,34]
sqre = np.sqrt(fib)

Write a program to plot Fibonacci terms and their square root with two separate line.
(with different types of markers) 
"""

import matplotlib.pyplot as plt
import numpy as np

fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
sqfib = np.sqrt(fib)

plt.plot(range(1, 11), fib, linestyle="solid")
plt.plot(range(1, 11), sqfib, linestyle="dashed")
plt.show()
