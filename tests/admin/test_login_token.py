# 登陆并获取token
import allure
import requests

from utils.yaml_handler import YamlHandler


@allure.feature("admin:登录后返回token")
@allure.link("/admin/login")
def test_admin_login_token(get_evn):
    host = get_evn["host"]
    path = "/admin/login"
    content_type = {"Content-Type": "application/json"}
    headers = {**get_evn["headers"],**content_type}
    # 权限用户token
    data_1 = {
        "username": "admin",
        "password": "macro123"
    }
    # 非权限token
    data_2={
        "username":"123456",
        "password":"123456"
    }

    r_1 = requests.request("POST", url=host + path, headers=headers, json=data_1)
    response_1 = r_1.json()

    r_2 = requests.request("POST", url=host + path, headers=headers, json=data_2)
    response_2 = r_2.json()

    token=[response_1["data"],response_2["data"]]

    yamlHander = YamlHandler("E:/code/python/mall_tiny_test/data/admin/token.yaml")
    # 将得到的token和tokneHead存入yaml文件
    yamlHander.write_yaml(token)
