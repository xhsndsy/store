import requests
######################################1.登陆请求
def login():
    url_login = "http://localhost:8080/HKR/UserServlet"
    login_param = {
        "method":"login",
        "loginname":"jason",
        "password":"12345678"
    }
    #
    response = requests.post(url_login,data=login_param)

    status = response.status_code

    # 取出cookie
    cookies = response.cookies

    # cooks 是下一步要用的cookies数据
    cooks = ""
    for key,value in cookies.items():
        cooks =  cooks + "{0}={1};".format(key,value)
    #cooks =  JSESSIONID=CC882AE6CB0F6F19FDC971A9A6D30566; username=%E8%B4%BE%E7%94%9F;
    cooks = cooks[:-1] #JSESSIONID=CC882AE6CB0F6F19FDC971A9A6D30566; username=%E8%B4%BE%E7%94%9F
    return cooks

#################################################修改头像请求
cooks = login()

def modifyPicture():
    url = "http://localhost:8081/HKR/UserServlet?method=changePicture"
    hread ={
        "Content-Type": "application/json;charset=UTF-8",
        "Cookie":cooks
    }

    param = {"uid":"ffd73bf04aab43c587eaacb608f2ff68",
             "pid":"asd1f8a181fas8dfad8sf1a0fa5a05"}

    # 获取响应对象
    response = requests.post(url=url,json=param,headers=hread)

    status = response.status_code
    # 取出响应体
    content = response.text

    print("修改头像状态吗：",status)
    print("响应体：",content)

modifyPicture()







