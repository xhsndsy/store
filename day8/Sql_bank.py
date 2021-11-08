import random
import DBUtils

def bankUI():
    print("***************************")
    print("*    中国工商银行           *")
    print("*     账户管理系统          *")
    print("***************************")
    print(" ")
    print("*1.开户                   *")
    print("*2.存钱                   *")
    print("*3.取钱                   *")
    print("*4.转账                   *")
    print("*5.查询                   *")
    print("*6.欢迎下次光临            *")
    print("**************************")
# 初始化银行
# 'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
# 定义一个开户银行
bank_name = "保熟银行"
# 定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd( name, account, password, country, province, steert, door):
    sql = 'select count(*) from user'
    param1 = []
    data = DBUtils.select(sql, param1, mode='one')

    sql2 = 'select * from user where name = %s'
    param2 = [name]
    data2 = DBUtils.select(sql2, param2)

    if data[0] >= 100:
        return 3
    elif len(data) >= 1:
        return 2
    else:
        param = [name, account, password, country, province, steert, door, 0, bank_name]
        DBUtils.update('insert into user values (%s, %s, %s, %s, %s, %s, %s, %s, %s)', param)
        return 1


# 定义用户入参
def useradd():
    account = random.randint(10000000, 99999999)
    name = input("请输入您的名称")
    password = int(input("请输入您的密码"))

    # 判断密码是否为6位
    if 100000 < password < 999999:
        pass
    else:
        password = int(input("请输入6位数字的密码密码"))
    print("请输入你的详细信息")
    country = input("\t\t请输入您的国籍")  # \t ==tab
    province = input("\t\t请输入您的省份")
    steert = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    num = bankadd(name, account, password, country, province, steert, door)

    if num == 3:
        print("本银行已满请到其他银行开户")
    elif num == 2:
        print("用户已存在")
    elif num == 1:
        print("恭喜你开户成功，以下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%s
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        sql = 'select * from user where name = %s'
        param = [name]
        data = DBUtils.select(sql, param)
        for i in data:
            print(i)
        return 1


# 存钱
def saving(account, money):
    sql1 = 'select * from user where name = %s'
    param = [account]
    data1 = DBUtils.select(sql1,param)
    if len(data1) == 0:
        return False
    else:
        sql2 = 'update user set money = money + %s where name = %s'
        param2 = [money, account]
        DBUtils.update(sql2, param2)
        print('您的当前余额为', DBUtils.select(sql1,param))


# 取钱
def out_money(account, password, money):
    sql1 = 'select name from user where name = %s'
    param1 = [account]
    data1 = DBUtils.select(sql1, param1)

    sql2 = 'select password from user where name = %s'
    param2 = [password]
    data2 = DBUtils.select(sql2, param1)

    sql3 = 'select money from user where name = %s'
    param3 = [money]
    data3 = DBUtils.select(sql3, param1)
    if len(data1) == '':
        return 1

    elif data2[0][0] != password:
        return 2
    else:
        if data3[0][0] < money:
            return 3
        elif data3[0][0] >= money:
            sql4 = 'update user set money = money - %s'
            param4 = [money]
            DBUtils.update(sql4, param4)
            print('您的转出金额为', money)
            print('转账成功，您的当前余额为', DBUtils.select(sql3, param1))

            return 0



# 转账
def transfer(out_account, in_account, password, money):

    sql1 = 'select * from user where name = %s or name = %s'
    param1 = [out_account, in_account]
    data1 = DBUtils.select(sql1, param1)

    sql3 = 'select * from user where name = %s'
    param3 = [out_account]
    data3 = DBUtils.select(sql3, param3)

    if data1[0][0] is None or data1[1][0] is None:
        return 1

    elif data3[0][2] == password:
        if data3[0][7] < money:
            return 3
        elif data3[0][7]:
            sql2 = 'update user set money = money - %s where name = %s'
            param2 = [money, out_account]
            DBUtils.update(sql2, param2)

            sql3 = 'update user set money = money + %s where name = %s'
            param3 = [money, in_account]
            DBUtils.update(sql3, param3)
            return 0
    else:
        return 2

# 查询
def search(account, password):

    sql1 = 'select * from user where name = %s'
    param = [account]
    data1 = DBUtils.select(sql1, param)

    if data1[0] is None:
        print('用户不存在')
    elif data1[0][2] == password:
        info = '''
                           ------------个人信息------------
                           用户名:%s
                           账号：%s
                           密码：*****
                           国籍：%s
                           省份：%s
                           街道：%s
                           门牌号：%s
                           余额：%s
                           开户行名称：%s
                       '''

        print(info % (data1[0][0], data1[0][1], data1[0][3], data1[0][4], data1[0][5], data1[0][6], data1[0][7], data1[0][8]))

    else:
        print('密码错误')

while not 0:

    bankUI()
    index = int(input("请输入您需要的业务"))

    if index == 1:
        print("开户")
        useradd()

    elif index == 2:

        print("存钱")
        account = input('请输入存钱账号:')
        in_money = int(input('请输入存钱金额：'))
        saving(account, in_money)

    elif index == 3:

        print("取钱")
        account = input('请输入用户账号：')
        password = int(input('请输入用户密码：'))
        money = int(input('请输入取钱金额:'))

        out = out_money(account, password, money)

        if out == 1:
            print('账号不存在')
        elif out == 2:
            print('密码错误')
        elif out == 3:
            print('余额不足')
        elif out == 0:
            pass

    elif index == 4:
        print("转账")

        # 获取输入值
        out_account = input('请输入您想要转出的账号:')
        in_account = input('转入账号：')
        password = int(input('请输入转出账号的密码：'))
        money = int(input('请输入转出的金额：'))

        # 获取函数返回值
        re = transfer(out_account, in_account, password, money)

        # 执行判断返回值
        if re == 1:
            print('转出或转入的账号不存在')
        elif re == 2:
            print('密码错误')
        elif re == 3:
            print('余额不足')
        elif re == 0:
            sql1 = 'select money from user where name = %s'
            param = [out_account]
            data1 = DBUtils.select(sql1, param)
            print('当前账户余额为', data1[0][0])
            print('转账金额', money)

            sql2 = 'select money from user where name = %s'
            param = [in_account]
            data2 = DBUtils.select(sql2, param)

            print('收款账户余额为', data2[0][0])

    elif index == 5:
        print("查询")

        account = input('请输入账户号')
        password = int(input('请输入密码'))

        search(account, password)


    elif index == 6:
        print("下次光临")
        break