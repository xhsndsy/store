import math

def perimeter(radius):
    peim = radius*2*math.pi
    return peim

def acreage(radius):
    acre = radius*radius*math.pi
    return acre

if __name__ == '__main__':

    print("请输入半径")
    radius = int(input())
    print("周长",perimeter(radius))
    print("面积",acreage(radius))