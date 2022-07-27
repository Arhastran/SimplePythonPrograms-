import matplotlib.pyplot as plt
import numpy as np
import random
"""
List comprehension 
"""

numbers = [i+1 for i in range (6)] #skrót do generacji listy z liczbami

numbers2 = [i**2 for i in range (11)] #kwadraty liczb od 0 do 10

numbers3 = [i**2 for i in range (11) if i % 2 == 0] #parzyste

numbers4 = [i**2 if i % 2 ==0  else 0 for i in range (11)] #parzyste + reszta na zero

numbers5 = [i-5 for i in range(100) if i>=18]

numbers6 = [5*i-2 if i % 2 == 0 else random.random() for i in range (101)]

#wykresy


plt.plot(numbers3, 'r-',numbers4, 'gD', numbers5,'bD')

plt.show()
