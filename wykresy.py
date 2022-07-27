"""
Wykresy
"""

import matplotlib.pyplot as plt
import numpy as np
import random

numbers = [5, 10, 15, 3, 25]
#plt.plot(numbers, 'mp--') #bD: , r-, k*, g^

###################
x = [i+1 for i in range (-10,10)]
y = [5*i-2 for i in x]
y2 = [-2*i+5 for i in x]
y3 = [3*i+3 for i in x]
plt.plot(x,y, 'rD-', x,y2, 'b^-', x,y3,'gs-')
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("First plot")
plt.show()
