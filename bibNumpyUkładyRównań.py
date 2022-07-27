"""
macierze
"""

import numpy as np


A=np.array([[2,3],[4,1]])
B=np.array([12,14])
XY=np.linalg.solve(A,B)
XY1 = np.linalg.inv(A) @ B #to samo co solve ale przy użyciu odwracania

#solve nie rozwiązuje układów sprzeczynch

C = ([[2,3],[6,9]])
D = ([2,6])
if np.linalg.det(C):
    XY2 = np.linalg.solve(A,B)
    print(XY2)
else:
    print("Układ sprzeczny")

