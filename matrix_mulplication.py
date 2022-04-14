from input import *
from sympy import *
from sympy.solvers.solveset import linsolve


def mul(mat_a, mat_b):
    return mat_a @ mat_b


def main():
    datatype = input_datatype()
    print("计算矩阵乘法A @ B，输入矩阵A：")
    mat_a = input_matrix(datatype=datatype)
    print("计算矩阵乘法A @ B，输入矩阵B：")
    mat_b = input_matrix(datatype=datatype)
    r = mul(mat_a, mat_b)
    print("矩阵乘法计算结果为：\n", r)
    return r


if __name__ == '__main__':
    main()
