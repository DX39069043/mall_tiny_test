# 登陆并获取token

import requests

from utils.yaml_handler import YamlHandler


def test_admin_login_token(get_evn):
    host = get_evn["host"]
    path = "/admin/login"
    data = {
        "username":"admin",
        "password":"macro123"
    }
    headers = get_evn["headers"]
    r = requests.request("POST", url=host + path, headers=headers, json=data)
    response = r.json()
    yamlHander = YamlHandler("E:/code/python/mall_tiny_test/data/token.yaml")
    # 将得到的token和tokneHead存入yaml文件
    yamlHander.write_yaml(response["data"])
