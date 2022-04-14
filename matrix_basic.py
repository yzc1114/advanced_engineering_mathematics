import numpy as np
from input import *

def matrix_inv(A):
    assert np.linalg.matrix_rank(A) == len(A), f'矩阵奇异，不可对角化'
    return np.linalg.inv(A)


def matrix_mul(A, B):
    return np.matmul(A, B)


def matrix_pow(A, n):
    B = np.eye(len(A))
    for i in range(n):
        B = matrix_mul(A, B)
    return B
