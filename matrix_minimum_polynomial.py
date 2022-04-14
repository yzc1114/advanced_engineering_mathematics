import sympy

from input import *
from sympy import *
from sympy.solvers.solveset import linsolve
from itertools import permutations


def minimum_polynomial(mat: np.ndarray):
    w = mat.shape[0]
    m = Matrix(mat)
    eigen_values = m.eigenvals()
    # print(f"矩阵的特征值为：{eigen_values}")
    eigen_values_list = []
    for k, v in eigen_values.items():
        print(f"特征值：{k}, 特征值重复次数：{v}")
        eigen_values_list.append(k)
    print(f"共有{len(eigen_values_list)}个特征值（包含重复的）")
    print(f"接下来，从1重特征值开始遍历，直到{len(eigen_values_list)}重特征值的组合。")
    for m in range(len(eigen_values_list)):
        print(f"对{m+1}重特征值开始遍历")
        for permutation in permutations(eigen_values_list, m+1):
            print("当前特征值排序：", permutation)
            eqs = []
            for eigen_value in permutation:
                eqs.append(mat - eigen_value * eye(w))
            multiplication = None
            for eq in eqs:
                if multiplication is None:
                    multiplication = eq
                else:
                    multiplication = multiplication @ eq
            # print(type(multiplication))
            result = np.array(multiplication).astype(mat.dtype)
            result = round_matrix(result)
            print(f"结果为：\n{result}")
            if not np.any(result):
                print(f"找到最小多项式的特征值为：{permutation}")
                print("该最小多项式对应的连乘矩阵分别为：")
                for i, eq in enumerate(eqs):
                    print(f"方阵{i}为：\n", np.array(eq))
                return


def main():
    datatype = input_datatype()
    print("计算矩阵的最小多项式，首先输入方阵：")
    w = int(input("请输入方阵的宽度："))
    mat = input_matrix(m=w, n=w, datatype=datatype)
    minimum_polynomial(mat)


if __name__ == '__main__':
    main()
