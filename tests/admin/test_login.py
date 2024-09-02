# 登录
import pytest
import requests

from utils import yaml_handler

yamlhandler_data = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/login_data.yaml")
login_data = yamlhandler_data.read_yaml()

@pytest.mark.parametrize("case",login_data)
def test_login_data(case, get_evn):

    host = get_evn["host"]
    # path = "/admin/login"
    path = case["URL"]
    headers = get_evn["headers"]
    r = requests.request("POST", url=host + path, headers=headers, json=case["请求体"])
    assert case["预期结果"] == r.json()["message"]



yamlhandler_param = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/login_param.yaml")
login_param = yamlhandler_param.read_yaml()

@pytest.mark.parametrize("case", login_param)
def test_login_param(case,get_evn):

    host = get_evn["host"]
    # path = "/admin/login"
    path = case["URL"]
    headers = get_evn["headers"]
    r = requests.request("POST", url=host + path, headers=headers, json=case["请求体"])
    if "message" in r.json():
        assert r.json()["message"] == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]

