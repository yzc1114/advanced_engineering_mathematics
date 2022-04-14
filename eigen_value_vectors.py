from input import *
from matrix_basic import *


if __name__ == '__main__':
    A = input_matrix()
    w, v = np.linalg.eig(A)
    print("特征值为：")
    print(w)
    print("每个特征值对应的特征向量为（按列）：")
    print(v)
    P = v
    P_inv = matrix_inv(P)
    print("P矩阵为：")
    print(round_matrix(v))
    print("P矩阵的逆为：")
    print(round_matrix(P_inv))
    D = matrix_mul(matrix_mul(P_inv, A), P)
    print("对角矩阵D为：")
    print(round_matrix(D))


### 测试样例
# 3
# 3
# 0 1 0
# 0 0 1
# -6 -11 -6



###