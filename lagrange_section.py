def Lagrange_section():
    print("拉格朗日_分段抛物插值")
    print("输入三个点：")
    l1 = input()
    l2 = input()
    l3 = input()
    a, b = l1.split()
    c, d = l2.split()
    e, f = l3.split()
    x1 = float(a)
    x2 = float(c)
    x3 = float(e)
    y1 = float(b)
    y2 = float(d)
    y3 = float(f)

    # 1.9881 1.4100
    # 2.0164 1.4200
    # 2.0252 1.4231
    
    print("输入要拟合的数据点：", end="")
    x = float(input())
    f = float(0)
    f += ((x - x2) * (x - x3) * y1) / ((x1 - x2) * (x1 - x3))
    f += ((x - x1) * (x - x3) * y2) / ((x2 - x1) * (x2 - x3))
    f += ((x - x1) * (x - x2) * y3) / ((x3 - x1) * (x3 - x2))
    print("拟合结果为：", end="")
    print(f)

if __name__ == '__main__':
    Lagrange_section()