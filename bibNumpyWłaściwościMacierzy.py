"""
macierze
"""

import numpy as np
import random
import math

A = np.array([[1,2],[3,4]])
detA1= np.linalg.det(A) #wyznacznik
#detA2= A[0,0]*A[1,1]- A[0,1]*A[1,0]
traceA1 = np.trace(A) #ślad
traceA2 = np.sum(np.diagonal(A))

B = np.array([[2,3,5], [-1,4,6], [3,-2,7]])
detB = np.linalg.det(B)
print(detB)
