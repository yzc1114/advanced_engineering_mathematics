import decimal
from decimal import Decimal
import numpy as np

decimal.getcontext().rounding = "ROUND_HALF_UP"


def list_to_decimal(l):
    l = [Decimal(x) for x in l]
    return l


def input_list_decimal(prompt, k=None):
    return input_list(prompt, Decimal, k=k)


def input_list(prompt, as_type, k=None):
    ns = list(map(lambda n: as_type(n), input(prompt).split()))
    if k is not None:
        assert len(ns) == k, f'输入数据长度应为{k}, 您输入的数据长度为{len(ns)}'
    return ns


def input_list_float(prompt, k=None):
    return input_list(prompt, as_type=float, k=k)


def round_decimal(dec, n=4):
    return dec.quantize(Decimal('0.' + '0'*n))


def input_datatype():
    datatype_int = int(input("输入数据类型：(0代表整数，1代表浮点数，2代表复数）"))
    m = {
        0: int,
        1: float,
        2: complex
    }
    if datatype_int not in m:
        assert False, '输入有误'
    return m[datatype_int]

def input_matrix(m=None, n=None, datatype=float) -> np.ndarray:
    print("输入矩阵：")
    if m is not None:
        print(f"输入矩阵宽度，已确定为：{m}")
    else:
        m = int(input("输入矩阵宽度："))
    if n is not None:
        print(f"输入矩阵高度，已确定为：{n}")
    else:
        n = int(input("输入矩阵高度："))
    print(f"按行输入数据，共{n}行，{m}列：")
    ls = []
    for i in range(n):
        ls.append(input_list(f"输入第{i+1}行：", as_type=datatype, k=m))
    a = np.asarray(ls)
    print(f"您输入的矩阵为：\n{a}")
    return a


def as_matrix(ls) -> np.ndarray:
    return np.asarray(ls)


def round_matrix(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            if -1e-7 < A[i][j] < 1e-7:
                A[i][j] = 0
    return A


if __name__ == '__main__':
    input_matrix()
