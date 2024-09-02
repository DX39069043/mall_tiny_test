# 根据不同的数据，测试登陆接口
import pytest
import requests

from utils import yaml_handler

yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/login_data.yaml")

login_data = yamlhandler.read_yaml()
print(login_data)


@pytest.mark.parametrize("case",login_data)
def test_login(case):

    host = "http://localhost:8080"
    # path = "/admin/login"
    path = case["URL"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
        "Content_Type": "application/json"
    }
    r = requests.request("POST", url=host + path, headers=headers, json=case["请求体"])
    assert case["预期结果"] == r.json()["message"]
