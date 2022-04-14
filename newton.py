from input import *


def newton(x, y):
    x = [Decimal(x) for x in x]
    y = [Decimal(y) for y in y]
    assert len(x) == len(y)
    ls = [x, y]
    for i in range(len(x) - 1):
        column = []
        last_column = ls[i+1]
        first_column = ls[0]
        size = len(x) - 1 - i
        for n in range(size):
            up = last_column[n+1] - last_column[n]
            bottom = first_column[n+i+1] - first_column[n]
            value = up/bottom
            value = round_decimal(value, round_digits)
            column.append(value)
        ls.append(column)
    print(ls)
    for i in range(len(x)):
        for col_idx, col in enumerate(ls):
            if len(col) >= len(x)-i:
                print('%8s' % (col[i-(len(x)-len(col))]), end=' ')
        print('\b\n')


round_digits = 4


def main():
    k = int(input("输入点的个数："))
    x = input_list_decimal("输入x：", k=k)
    y = input_list_decimal("输入y：", k=k)
    print("您输入的x为：", x)
    print("您输入的y为：", y)
    newton(x, y)


if __name__ == '__main__':
    # main()
    # newton(['0.4', '0.55', '0.65', '0.80', '0.90', '1.05'], ['0.41075', '0.57815', '0.69675', '0.88811', '1.02652', '1.25385'])
    newton(['-2', '-1', '0', '1', '2'], ['-3', '-1', '1', '3', '29'])
