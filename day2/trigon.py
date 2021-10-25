import math

def per(length1, length2, length3):
    if length1>0 and length2>0 and length3>0 and length1+length2>length3 and length1+length3>length2 and length3+length2>length1:
        return '周长',length1 + length2 + length3
    else:
        return '此三条边无法构成三角形'

def acr(length1, length2, length3):
    if length1>0 and length2>0 and length3>0 and length1+length2>length3 and length1+length3>length2 and length3+length2>length1:

        p = (length1 + length2 + length3 ) / 2
        s = math.sqrt( p*(p-length1)*(p-length2)*(p-length3) )

        return '面积',s



if __name__ == '__main__':
    print('请输入三角形三条边长')
    a = int(input())
    b = int(input())
    c = int(input())
    print(per(a, b, c))
    print(acr(a, b, c))
