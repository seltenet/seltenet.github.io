# api_url = https://114.selte.net/jeecg-boot/contacts/list
# jeecg python login
# https://114.selte.net/jeecg-boot/sys/randomImage/1677349925426?_t=1677349925
import requests
import json
import time

login_url = "https://114.selte.net/jeecg-boot/sys/login"
url = "https://114.selte.net/jeecg-boot/contacts/list"
randomImage_url = "https://114.selte.net/jeecg-boot/sys/randomImage"

# 1677349925426?_t=1677349925
timestamp = str(int(time.time() * 1000))
print(timestamp)

randomImage_url = randomImage_url + "/" + timestamp + "?_t=" + timestamp
print(randomImage_url)
'''
https://114.selte.net/jeecg-boot/sys/randomImage/1677350091008?_t=1677350091008
{'success': True, 'message': '', 'code': 0, 'result': 'data:image/jpg;base64,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', 'timestamp': 1677350091635}
{'success': False, 'message': '验证码无效', 'code': 500, 'result': None, 'timestamp': 1677350091987}
'''


# get code from data:image/jpg;base64 which is randomImage_url's response
def get_code_from_base64(base64_str):
    imgdata = base64.b64decode(base64_str)
    file = open('code.jpg', 'wb')
    file.write(imgdata)
    file.close()
    return pytesseract.image_to_string(Image.open('code.jpg'))


# 获取验证码
def get_randomImage():
    response = requests.request("GET", randomImage_url)
    return response.json()


print(get_randomImage())


# 登录
def login(username, password):
    payload = json.dumps({
        "username": username,
        "password": password,
        "code": "1234",
        "key": "1234"
    })
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST",
                                login_url,
                                headers=headers,
                                data=payload)
    return response.json()


print(login("admin", "Ee123456"))

payload = json.dumps({
    "current": 1,
    "size": 10,
    "name": "张三",
    "phone": "13800138000",
    "email": "sdf@sdf.com",
    "address": "北京市朝阳区",
    "remark": "备注",
    "createBy": "admin",
    "createTime": "2020-12-01 00:00:00",
    "updateBy": "admin",
    "updateTime": "2020-12-01 00:00:00",
    "delFlag": "0"
})
# x-access-token in header
headers = {
    'Content-Type': 'application/json',
    'X-Access-Token': login("admin", "Ee123456")
}
response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
