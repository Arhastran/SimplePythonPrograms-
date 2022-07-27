"""
dopasowanie do danych z Prawa Hooka
"""

from scipy import stats
import random
import matplotlib.pyplot as plt
import numpy as np

F= [9.81, 19.62, 29.43, 39.24, 49.05, 58.86, 68.67, 78.48, 88.29, 98.10]
dL = [0.240, 0.420, 0.568, 0.705, 0.828, 0.953, 1.075, 1.208, 1.318, 1.430]

a, b, r_value, p_value, std_err =stats.linregress(dL,F)

Freg = [a*x+b for x in dL]
#print(X,Y)
plt.plot(dL,F, "ro", dL, Freg, "b--")
plt.show()