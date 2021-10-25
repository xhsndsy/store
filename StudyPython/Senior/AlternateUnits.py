def inch(cm):
    inc = cm*0.39
    return inc

def cm(inch):
    cm = inch*2.54
    return cm

if __name__ == '__main__':
    print("请输入您想要换算的单位(1 or 2)")
    print("1.英寸换算成厘米")
    print("2.厘米换算成英寸")

    unit = input()

    if unit == '1':
        inc = int( input('请输入长度') )
        print('换算后',cm(inc))

    if unit == '2':
        c = int( input('请输入长度') )
        print('换算后', inch(c))