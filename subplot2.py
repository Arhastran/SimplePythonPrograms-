"""
Cztery różne wykresy
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import math


x1 = [x for x in range (0,361,10)]
y1 = [math.sin(math.radians(x)) for x in x1]

plt.subplot(2,2,1)
plt.plot(x1,y1, 'g*--')

x2 = [x+1 for x in range (100)]
y2 = [random.random() for x in x2]
plt.subplot(2,2,2)
plt.plot(x2,y2, 'bp')

x3 = [x+1 for x in range (-5,5)]
y3 = [x**2-x-2 for x in x3]
plt.subplot(2,2,3)
plt.plot(x3,y3, 'rD-')

expenses=["mieszkanie", "media", "jedzenie","rozrywka","nauka","inwestycja"]
values=[3000,500,1600,500,200,500]
plt.subplot(2,2,4)
plt.pie(values,labels=expenses, autopct="%.2f %%")

plt.show()