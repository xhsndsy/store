def Christian():
    per = 15
    chr = 15
    count = 1
    while per > 0 :
        if (per+chr) % 9 == 0:
            print('非')
            count = count + 1
            per = per - 1
        else:
            print('基')
            count = count + 1
            chr = chr - 1


if __name__ == '__main__':
    Christian()
