if __name__ == '__main__':
    times = 1

    f = open('./black_user.txt','r')
    lock_username = f.read()
    f.close()


    while True:
        username = input('请输入用户名')
        password = input('请输入密码')

        if lock_username == username:
            print('此用户已被锁定，')
            continue
        elif times == 3:
            print('对不起，您输入的密码错误次数已经达到3次，您的用户名将被锁定')
            f = open('./black_user.txt','w')
            f.write('%s'%username)
            f.close()
            times = 1
            f = open('./black_user.txt', 'r')
            lock_username = f.read()
            f.close()
            continue
        elif username != 'root':
            print('用户名输入错误')
            times += 1
            continue
        elif password != 'admin':
            print('密码输入错误！')
            times += 1
            continue
        else:
            print('登录成功！')
            break
