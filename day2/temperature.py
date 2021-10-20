def temp(tem):
    tempe = (tem-32)/1.8
    return tempe

if __name__ == '__main__':

    print(temp(int(input("请输入华氏度"))))