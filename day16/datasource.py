import xlrd

class InitPage:
    file = 'HKR.xls'

    data = xlrd.open_workbook_xls(file)

    success_dic = {
        'name': '',
        'password': '',
        'expect': ''
    }
    error_dic = {
        'name': '',
        'password': '',
        'expect': ''
    }

    # 登录成功用例

    success = data.sheet_by_index(0)


    loginsuccessdata = []



    for i in range(1, success.nrows):
        success_dic['name'] = success.cell_value(i, 0)
        success_dic['password'] = success.cell_value(i, 1)
        success_dic['expect'] = success.cell_value(i, 2)
        loginsuccessdata.append(success_dic)
    # 登录失败用例

    error = data.sheet_by_index(1)
    loginerrordata = []

    for i in range(1, error.nrows):
        error_dic['name'] = error.cell_value(i, 0)
        error_dic['password'] = error.cell_value(i, 1)
        error_dic['expect'] = error.cell_value(i, 2)
        loginerrordata.append(error_dic)


    def getloginSuccessData(self):
        return self.loginsuccessdata

    def getloginErrorData(self):
        return self.loginerrordata