def leap(year):
    if year%4 == 0:
        return '闰年'
    else:
        return '不是闰年'

if __name__ == '__main__':
    year = int(input('请输入您想要输入的年份：'))
    print(leap(year))