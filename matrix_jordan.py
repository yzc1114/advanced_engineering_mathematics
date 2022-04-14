import numpy as np
import sympy as sp
import pprint
from input import *
from matrix_basic import *

A = input_matrix()
a = sp.Matrix(A)
P, Ja = a.jordan_form()

print("Jordan矩阵为：", end="")
print(Ja)
print("变换所需的P矩阵为：", end="")
print(P)
