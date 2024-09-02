# 使用不同的数据，测试注册接口

import pytest
import requests

from utils import yaml_handler

yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/register_data.yaml")

login_data = yamlhandler.read_yaml()
print(login_data)


@pytest.mark.parametrize("case",login_data)
def test_login(case,get_evn):

    host = get_evn["host"]
    # path = "/admin/register"
    path = case["URL"]
    headers = get_evn["headers"]
    r = requests.request("POST", url=host + path, headers=headers, json=case["请求体"])
    assert r.json()["message"] == case["预期结果"]
