"""
macierze
"""
#jakość spadła do 0 przez deszcz i nic nie napisałem
import numpy as np
import random
import math

B = np.array([[1,2,90], [2,3,4], [4,5,6]])
I = B@np.linalg.inv(B)
print(I)