import math

def IsTriangle(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return '不符合条件，请重新输入a,b,c'
    elif a+b<=c or abs(a-b)>=c:
        return '不是三角形'
    elif math.sqrt(a * a + b * b + c * c):
        return '直角三角形'
    elif a == b & a == c & b == c:
        return '这个三角形是等边三角形'
    elif a == b or a == c or b == c:
        return '等腰三角形'
    elif a == b and b == c and a == c:
        return '等边三角形'
    else:
        return '一般三角形'

if __name__ == '__main__':
    print('请输入三角形三条边')

    a = int(input())
    b = int(input())
    c = int(input())

    print(IsTriangle(a,b,c))