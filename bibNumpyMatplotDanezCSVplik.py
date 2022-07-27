"""
dane z Pliku csv
"""

import numpy as np
import matplotlib.pyplot as plt

data=[]
with open("dane.csv") as file:
    lines = file.readlines()
    data = np.genfromtxt(lines, delimiter = ",", skip_header = 1 )

    wiek = data[:,1]

    print("Mediana wieku:", np.median(wiek))

    wzrost = data[:,3]
    print ("Średnia wzrostu:" , np.mean(wzrost))

    waga = data[:,2]
    print ("Średnia waga:" , np.mean(waga), "Odchylenie:" , np.std(waga))

    R = np.corrcoef(wzrost, waga)  # oblicza się macierz a musimy znaleźć współczynnik korelacji
    print(np.linalg.det(R))

    plt.scatter(wzrost, waga, c='green')
    plt.xlabel("Wzrost")
    plt.ylabel("Waga")
    plt.show()


