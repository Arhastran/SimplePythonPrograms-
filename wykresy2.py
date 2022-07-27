"""
Słupkowe
"""

import matplotlib.pyplot as plt
import numpy as np
import random

names = ["Adam", "Bartosz", "Oliwia", "Remigiusz", "Sara"]
ages = [random.randint(18,70) for i in names]

plt.bar(names, ages, color=['red','green','blue'])
plt.xticks(names)
plt.yticks(ages)
plt.show()