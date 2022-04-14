from input import *
from sympy import *
from sympy.solvers.solveset import linsolve


def solve_lin(mat: np.ndarray):
    c = mat.shape[1]
    x_c = c-1
    print(f"增广矩阵共有{c}列，共有{x_c}个未知数")
    xs = symbols(', '.join([f'x{i+1}' for i in range(x_c)]))
    print(f"未知数符号分别为：{xs}")
    M = Matrix(mat)
    system = M[:, :-1], M[:, -1]
    result = linsolve(system, *xs)
    print(f"符号求解结果为：{result}")


def main():
    print("线性方程组求解Ax = b，请输入A与b的增广矩阵：")
    mat = input_matrix()
    # mat = np.asarray([[1., 1., 1., 1.], [1., 1., 2., 3.]])
    solve_lin(mat)


if __name__ == '__main__':
    main()
