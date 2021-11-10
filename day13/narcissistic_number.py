def narcissistic_num(num):
    if 100 <= num <= 1000:
            gewei = num % 10
            shiwei = num // 10 % 10
            baiwei = num // 100
            if gewei ** 3 + shiwei ** 3 + baiwei ** 3 == num:
                return '这个数是水仙花数'
            else:
                return '这个数不是水仙花数'
    else:
        return '这个数不在100到1000之内'



if __name__ == '__main__':
    print(narcissistic_num(1))  # 153, 370, 371, 407