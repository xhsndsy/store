import math


def IsPrime(n):
    if n <= 1:
        return '此函数不是素数'
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return '此函数不是素数'
    return '此函数是素数'

