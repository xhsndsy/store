# # 求根公式
# import math
#
#
# def sort1(a, b, c):
#     x1 = 0
#     x2 = 0
#
#     f = b ** 2 - 4 * a * c
#
#     if a == 0 | f >= 0:
#
#         return '此方程无解'
#
#     elif f == 0:
#
#         x1 = 0
#         x2 = 0
#         print('此方程有两个相同的实数根')
#         return x1
#
#     else:
#         x1 = (-b+math.sqrt(f))/(2*a)
#         x2 = (-b-math.sqrt(f))/(2*a)
#         return x1, x2
#
#
# print(sort1(3, 4, 5))
# print(sort1(0, 0, 0))
# print(sort1(1, 0, 0))
#
# #   测试用例    输入数据      预期结果
# #   用例1      1，2，3      (0.5, -1.5)
# #   用例2      0，0，0      此方程无解
# #   用例3      1，0，0      x1 , x2 的解为0

# print('Hello World!')
# def sort(num, type):
#     x = 0
#     y = 0
#     while num > 0:
#         if type == 0:
#             x = y + 2
#             num = num - 1
#         elif type == 1:
#             x = y + 10
#             num = num - 1
#         else:
#             x = y + 20
#             num = num - 1
#     return x


# if __name__ == "__main__":
#     # print(sort(5, 1))
#     # print(sort(1,0))
#     # print(sort(1,1))
#     # print(sort(1,10))
#     # print(sort(0,0))
#     # print(sort(0,1))
#     print(sort(5, 2))

import math

# def add(a, b):
#     c = a + b
#     return c
#
#
# print(add(-1, -1))
# print(add(-1, 0))
# print(add(-1, 1))
# print(add(0, 0))
# print(add(0, 1))
# print(add(1, 1))


# sqrt
# def a(x):
#     if x < 0:
#         # print("该数无平方根！")
#         pass
#     else:
#         x = math.sqrt(x)
#     return x
#
# print(a(4))
# print(a(-4))
# print(a(0)


# import math
#
#
# def a(a, b, c):
#     x1 = 0
#     x2 = 0
#     d = b * b - 4 * a * c
#     if a == 0:
#         return "方程不是一元二次方程"
#     else:
#         if d < 0:
#             return "方程无实根"
#             pass
#         else:
#             x1 = (-b + math.sqrt(d)) / (2 * a)
#             x2 = (-b - math.sqrt(d)) / (2 * a)
#     return x1, x2
#
#
# print(a(0, 1, 2))
# print(a(1, 1, 2))
# print(a(2, 4, 2))
# a(1, 2, 1)

# import math


# def a(x, y):
#     if x == y:
#         print('可以构建圆形或正方形')
#     elif 2 < math.fabs(x - y) <= 5:
#         print('可以构建椭圆形')
#     elif math.fabs(x - y) > 5:
#         print('可以构建矩形')
#     else:
#         print('您输入的数据不在判断范围内')
#
#
# print(a(1, 2))
# print(a(1, 1))
# print(a(2, 5))
# print(a(1, 7))


import math
def sjx(a,b,c):
    if a<=0 or b<=0 or c<=0:
        return '不符合条件，请重新输入a,b,c'
    elif a+b<=c or abs(a-b)>=c:
        return '不是三角形'
    elif a == b & a == c & b == c:
        return '这个三角形是等边三角形'
    elif a == b or a == c or b == c:
        return '等腰三角形'
    elif a == b and b == c and a == c:
        return '等边三角形'
    else:
        return '一般三角形'

# x = int(input('请输入a的值:'))
# y = int(input('请输入b的值:'))
# z = int(input('请输入c的值:'))

# print(sjx(x,y,z))
