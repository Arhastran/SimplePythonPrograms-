"""
całki numeryczne
"""

from scipy import integrate
import math
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 3*x**2+1


def f2(x):
    return math.cos(x)


def f3(x):
    return -x**2 +7*x -10

V,err= integrate.quad(f,0,1)
I,err2 = integrate.quad(f2, 0 ,math.pi/2)

X = range(10)
Y = [f3(x) for x in X]

I3, err3 = integrate.quad(f3, 2, 5)
print(I3)

plt.plot(X,Y, 'r:')
plt.axhline()
plt.show()




