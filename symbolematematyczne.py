"""
Symbole
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import math

epsilon = [i for i in range(1,10)]
sigma = [math.log10(i) for i in epsilon]

plt.plot(epsilon,sigma)
plt.title(r"Wykres naprężęnia $\sigma (\delta \epsilon)$") #znaki greckie
plt.xlabel(r"$\frac{\delta\epsilon}{\epsilon}$", size=10) # ułamki
plt.ylabel(r"$\sigma$")
plt.text(5,0.8,r"$\sigma=f(\delta / \epsilon)$") #podpis funkcji
plt.show()

