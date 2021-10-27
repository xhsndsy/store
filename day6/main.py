import random

print("***************************")
print("*    中国工商银行          *")
print("*     账户管理系统         *")
print("***************************")
print(" ")
print("*1、开户                   *")
print("*2、存钱                   *")
print("*3、取钱                   *")
print("*4、转账                   *")
print("*5、查询                   *")
print("*6、欢迎下次光临            *")
print("****************************")
# 初始化银行
bank = {}
# 'Frank': {'account': 24275182, 'password': '123456', 'country': '中国', 'province': '山东', 'steert': '曹县', 'door': '001', 'money': 0, 'bank_name': '保熟银行'}
# 定义一个开户银行
bank_name = "保熟银行"


# 定义添加到银行 定义函数元素对应元素  不是名称对名称
def bankadd(account, name, password, country, province, steert, door):
    if len(bank) >= 100:
        return 3
    elif name in bank:
        return 2
    else:
        bank[name] = {
            "account": account,
            "password": password,
            "country": country,
            "province": province,
            "steert": steert,
            "door": door,
            "money": 0,
            "bank_name": bank_name
        }
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
    num = bankadd(account, name, password, country, province, steert, door)

    if num == 3:
        print("本银行已满请到其他银行开户")
    elif num == 2:
        print("用户已存在")
    elif num == 1:
        print("恭喜你开户成功，一下是您的相信信息")
        info = '''
                   ------------个人信息------------
                   用户名:%s
                   账号：%s
                   密码：*****
                   国籍：%s
                   省份：%sc 
                   街道：%s
                   门牌号：%s
                   余额：%s
                   开户行名称：%s
               '''
        # 每个元素都可传入%
        print(info % (name, account, country, province, steert, door, bank[name]["money"], bank_name))


# 存钱
def saving(account, money):
    if bank[account]['account'] is None:
        return False
    else:
        bank[account]['money'] += money


# 取钱
def out_money(account, password, money):
    if bank[account]['account'] == '':
        return 1
    elif bank[account]['password'] == password:
        if bank[account]['money'] < money:
            return 3
        elif bank[account]['money'] >= money:
            bank[account]['money'] = bank[account]['money'] - money
            return 0
    return 2


# 转账
def transfer(out_account, in_account, password, money):
    if bank[out_account]['account'] is None or bank[in_account]['account'] is None:
        return 1

    elif bank[out_account]['password'] == password:
        if bank[out_account]['money'] < money:
            return 3
        elif bank[out_account]['money']:
            bank[out_account]['money'] -= money
            bank[in_account]['money'] += money
            return 0
    else:
        return 2

# 查询
def search(account, password):

    if bank[account]['account'] is None:
        print('用户不存在')
    elif bank[account]['password'] == password:
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
        print(info % (account, bank[account]['account'], bank[account]['country'], bank[account]['province'], bank[account]['steert'], bank[account]['door'], bank[account]['money'], bank_name))
    else:
        print('密码错误')

while not 0:
    index = int(input("请输入您需要的业务"))

    if index == 1:

        print("开户")
        useradd()
        print(bank)

    elif index == 2:

        print("存钱")
        account = input('请输入存钱账号:')
        in_money = int(input('请输入存钱金额：'))
        saving(account, in_money)
        print('您的余额为：', bank[account]['money'])

    elif index == 3:

        print("取钱")
        account = input('请输入用户账号：')
        password = int(input('请输入用户密码：'))
        money = int(input('请输入取钱金额:'))

        print(bank[account]['password'])

        if out_money(account, password, money) == 1:
            print('账号不存在')
        elif out_money(account, password, money) == 2:
            print('密码错误')
        elif out_money(account, password, money) == 3:
            print('余额不足')
        elif out_money(account, password, money) == 0:
            bank[account]['money'] += money * 3
            print('您的余额为：', bank[account]['money'])

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
            print('当前账户余额为', bank[out_account]['money'])
            print('转账金额', money)
            print('收款账户余额为', bank[in_account]['money'])

    elif index == 5:
        print("查询")

        account = input('请输入账户号')
        password = int(input('请输入密码'))

        search(account, password)

    elif index == 6:
        print("下次光临")
        break
