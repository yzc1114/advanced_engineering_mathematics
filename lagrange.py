from scipy.interpolate import lagrange

def Lagrange_interpolation():
    print("拉格朗日插值")
    print("输入点的数量：")
    n = int(input())
    x = []
    y = []
    print("输入每个点：")
    for i in range(n):
        xy = input()
        xi, yi = xy.split()
        x.append(int(xi))
        y.append(int(yi))
    # x=[-2,-1,0,1,2]
    # y=[-3,-1,1,3,29]
    a=lagrange(x,y)
    print("插值函数为：")
    print(a)
    print("输入要拟合的数据点：", end="")
    data = int(input())
    print("拟合结果为：", end="")
    print(a(data))


if __name__ == '__main__':
    Lagrange_interpolation()