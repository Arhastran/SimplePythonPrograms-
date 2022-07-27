"""
macierze
"""

import numpy as np
import matplotlib.pyplot as plt

a = [0,45, 90, 180]
a =np.array(a)
print(np.radians(a)) #zmiana na radiany

a2 = np.array([-5.5, -1, 0 , 0.2, 10.123])
print(np.around(a2,2)) #zaokrąglenie do n po przecinku
print(np.floor(a2)) # w dół

#funkcje statystyczne

np.sum(a)
np.prod(a) #iloczyn elementów a
np.mean(a) #średnia elementów
np.median(a) #mediana
np.std(a) #odchylenie standardowe
np.var(a) #wariacja
np.min(a)
np.max(a)
np.argmin(a)
np.argmax(a)

#rozkłady statystyczne
mu = 3
sigma = 0.5
N = 10
x = np.random.normal(mu,sigma,N)
print(np.mean(x),np.median(x),np.std(x), np.var(x), np.min(x),np.argmin(x),np.max(x),np.argmax(x))

#narysuj histogram z 10 binami i sprawdzić, jak wygląda dla N=100

bins = 10
M = 1000
#plt.hist(x,bins,edgecolor='black')
#plt.show()

alpha = 2
beta = 5

Y=np.random.beta(alpha,beta,M)

V=(alpha*beta)/(alpha+beta)**2/(alpha+beta+1)
print(V) #do zgodności z wariacją
var=np.var(Y)
print(var)
plt.hist(Y,bins, edgecolor = 'black')
plt.show()




