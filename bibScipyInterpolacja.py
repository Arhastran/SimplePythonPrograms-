"""
interpolacja
"""

from scipy import interpolate
import random
import matplotlib.pyplot as plt
import numpy as np

x =np.arange(10)
y = np.exp(x/3)

plt.plot(x,y, 'ro')

f = interpolate.interp1d(x,y)
x2 = np.arange(0,9,0.1)
y2=f(x2)
plt.plot(x2,y2 ,'b--')
plt.show()