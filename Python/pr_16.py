"""
Write a program to plot a bar chart from the scores of four students in five different subjects. Make sure that
bars are separately visible. 
"""

import matplotlib.pyplot as plt

sub = ["English", "History", "IP", "Pscyhology", "Political Science"]
samaira = [89, 87, 96, 94, 91]
aryan = [67, 89, 56, 45, 67]
ashish = [56, 45, 52, 34, 57]
paras = [46, 32, 37, 48, 42]

plt.bar(sub, samaira, label="Samaira")
plt.bar(sub, aryan, label="Aryan")
plt.bar(sub, ashish, label="Ashish")
plt.bar(sub, paras, label="Paras")
plt.legend(loc=2)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()
