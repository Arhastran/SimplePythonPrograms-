"""
Histogram
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import math

data1 = [random.randint(0,20) for i in range(1000)] #1000 losowych liczb z zakresu 0-20
data2 = [random.gauss(mu=10, sigma=5) for i in range (1000)] #1000 losowych liczb z rozkładu Gaussa mu=10 sigma =5

bins = 10
plt.subplot(2,2,1)
plt.hist(data1, bins, edgecolor='black')

plt.subplot(2,2,2)
plt.hist(data2, bins, facecolor='red', edgecolor = 'black')


data3 = [random.gammavariate(alpha=10, beta=20) for i in range (1000)] #1000 liczb rozkład Gamma dla określonych k i theta
plt.subplot(2,2,3)
plt.hist(data3, bins, facecolor='green', edgecolor = 'black')

data4 = [random.gammavariate(alpha=5, beta=0.6) for i in range (1000)] #1000 liczb rozkład Gamma dla określonych k i theta
plt.subplot(2,2,4)
plt.hist(data4, bins, facecolor='yellow', edgecolor = 'black')


plt.show()