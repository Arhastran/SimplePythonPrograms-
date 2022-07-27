"""
regresja liniowa
losowa


NIE WIEM CO BO SIĘ INTERNET ZACIĄŁ NA DŁUGO :)
"""



from scipy import stats
import random
import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(1,10,num=10)
Y = np.random.randint(20, size= 10)
a, b, r_value, p_value, std_err =stats.linregress(X,Y)

plt.plot(X,Y,'ro-')

plt.show()