"""
Kołowe
"""

import matplotlib.pyplot as plt
import numpy as np
import random


expenses=["mieszkanie", "media", "jedzenie","rozrywka","nauka","inwestycja"]
values=[3000,500,1600,500,200,500]
explode = [0 for i in expenses]
# tu jest coś źle
explode[expenses.index("inwestycje")] = 0.1
plt.pie(values,labels=expenses, explode=explode, autopct="%.2f %%")
plt.show()