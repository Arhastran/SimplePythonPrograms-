"""
dane z Pliku
"""

import numpy as np
import matplotlib.pyplot as plt
#pobieranie z pliku i rozkładanie żeby mieć dane
data=[]
with open("data.txt") as file:
    lines = file.readlines()
    for line in lines:
        x,y = line.split(",")
        data.append( [int(x), int(y) ] )
X = [record[0] for record in data]
Y = [record[1] for record in data]
#plt.plot(X,Y, 'ro')
#plt.show()

#prostsze przy numpy
data2=[]
with open("data.txt") as file:
    lines = file.readlines()
    data2 = np.genfromtxt(lines, delimiter = ",")
    Y = data2[:,1]

    print(np.mean(Y), np.std(Y ),np.var(Y))


