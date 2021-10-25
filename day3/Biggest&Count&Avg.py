def biggest(num):
    big = 0
    for i in range(0,(len(num)-1)):
        if num[i]>num[i+1]:
            big = num[i]
        return big

def count(num):
    cou = 0
    for i in range(0,(len(num)-1)):
        cou = num[i] + cou
    return cou

def avg(num):
    ag = 0
    for i in range(0,(len(num)-1)):
        ag = count(num)/len(num)
    return ag


if __name__ == '__main__':
    num = []
    for i in range(0,10):
        n = int(input())
        num.append(n)

    print('最大值',biggest(num))
    print('求和',count(num))
    print('平均数',avg(num))
