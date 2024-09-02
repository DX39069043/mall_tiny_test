# 用户注册

import pytest
import requests

from utils import yaml_handler

yamlhandler_data = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/register_data.yaml")

login_data = yamlhandler_data.read_yaml()
print(login_data)

@pytest.mark.parametrize("case",login_data)
def test_register_data(case, get_evn):

    host = get_evn["host"]
    # path = "/admin/register"
    path = case["URL"]
    headers = get_evn["headers"]
    r = requests.request("POST", url=host + path, headers=headers, json=case["请求体"])
    assert r.json()["message"] == case["预期结果"]


yamlhandler_param = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/register_param.yaml")
login_param = yamlhandler_param.read_yaml()

@pytest.mark.parametrize("case", login_param)
def test_register_param(case,get_evn):

    host = get_evn["host"]
    # path = "/admin/register"
    path = case["URL"]
    headers = get_evn["headers"]
    r = requests.request("POST", url=host + path, headers=headers, json=case["请求体"])
    if "message" in r.json():
        assert r.json()["message"] == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]