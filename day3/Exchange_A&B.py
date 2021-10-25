def add(A,B):
    cache = A
    A = B
    B = cache
    return A,B

if __name__ == '__main__':
    print('A = 56')
    print('B = 78')
    print('请用 + or - 来实现A,B调换')
    print('输入 exit 退出')
    A = 56
    B = 78

    status = True

    while status:
        get = input()
        if get == '+':
            print(add(A,B))
        elif get == '-':
            print(add(B,A))
        elif get == 'exit':
            status = False
