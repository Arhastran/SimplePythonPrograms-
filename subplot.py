"""
Wykresy pod i obok siebie
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import math

x = [x for x in range (0,361,10)]
y1 = [math.cos(math.radians(x)) for x in x]
y2 = [random.random() for x in x]

plt.subplot(2,1,1)
plt.plot(x, y1, 'r.')

plt.subplot(2,1,2)
plt.plot(x, y2, 'bs:')

plt.show()
