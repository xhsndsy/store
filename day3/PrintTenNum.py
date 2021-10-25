

if __name__ == '__main__':
    print('请输入10个数')
    count = 0
    for num in range(0,10):
        getnum = int(input())
        count = count + getnum
    print(count)