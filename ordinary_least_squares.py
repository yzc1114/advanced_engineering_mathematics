from input import *
import numpy as np

"""
最小二乘法
"""


def ordinary_least_squares(x, y):
    assert len(x) == len(y)
    x = list_to_decimal(x)
    y = list_to_decimal(y)
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    x_square_sum = np.sum(np.square(x))
    cross_mul_sum = np.sum(np.multiply(x, y))
    n = len(x)
    a = (y_mean * x_square_sum - x_mean * cross_mul_sum) / (x_square_sum - n * (x_mean ** 2))
    b = (cross_mul_sum - n * x_mean * y_mean) / (x_square_sum - n * (x_mean ** 2))
    print('a = %s, b = %s' % (a, b))
    for i in range(len(x)):
        xi = x[i]
        yi = y[i]
        y_hat = a + b * xi
        print('a + b * %s = %s, y = %s, error = %s' % (xi, y_hat, yi, abs(yi-y_hat)))
    return a, b


def main():
    k = int(input('输入点的个数：'))
    x = input_list_decimal('输入x：', k=k)
    y = input_list_decimal('输入y：', k=k)
    a, b = ordinary_least_squares(x, y)


if __name__ == '__main__':
    main()
    # ordinary_least_squares(['19', '25', '31', '38', '44'], ['19.0', '32.3', '49.0', '73.3', '97.8'])
    # ordinary_least_squares([19**2, 25**2, 31**2, 38**2, 44**2], ['19.0', '32.3', '49.0', '73.3', '97.8'])
