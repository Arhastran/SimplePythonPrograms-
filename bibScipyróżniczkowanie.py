"""
różniczkowanie
"""

from scipy.misc import derivative
import math
import matplotlib.pyplot as plt
import numpy as np
from scipy import constants as con

def f(x):
    return -x ** 2 + 7 * x - 10


X = range(10)
Y = [f(x) for x in X]
plt.plot(X,Y)

print(derivative(f, x0=2, n=1))

print(con.speed_of_light, con.speed_of_sound, con.electron_mass, con.Planck)