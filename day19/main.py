'''
url:http://localhost:8081/HKR/UserServlet
请求方式：post




'''
import requests

url_login = "http://localhost:8081/HKR/UserServlet"
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

for key,value in cookies.items():
    print(key ,"=" ,value)

print(status)



