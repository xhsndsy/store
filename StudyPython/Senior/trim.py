def trim(s):
    if s == '':
        return s

    while s[0] == ' ':
        s = s[1:]
        if s == '':
            return s

    while s[len(s)-1] == ' ':
        s = s[:len(s)-1]
        if s == '':
            return s

    return s


if __name__ == '__main__':

    if trim('hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello') != 'hello':
        print('测试失败!')
    elif trim('  hello  ') != 'hello':
        print('测试失败!')
    elif trim('  hello  world  ') != 'hello  world':
        print('测试失败!')
    elif trim('') != '':
        print('测试失败!')
    elif trim('    ') != '':
        print('测试失败!')
    else:
        print('测试成功!')