# 登录
import allure
import pytest
import requests

from utils import yaml_handler

yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/list.yaml")

list_data = yamlhandler.read_yaml()["data"]
list_param=yamlhandler.read_yaml()["param"]

@allure.feature("admin:根据用户名或姓名分页获取用户列表")
@allure.link("/admin/list")
@pytest.mark.parametrize("case", list_data)
def test_login_data(case, get_evn, get_token, get_root_token):
    host = get_evn["host"]
    headers = get_evn["headers"]
    if case["用例标题"] == "没有相关权限":
        headers["Authorization"] = get_token
    else:
        headers["Authorization"] = get_root_token
    path = case["URL"]
    method = case["请求方法"]

    r = requests.request(method, url=host + path, headers=headers, json=case["请求体"])
    assert case["预期结果"] == r.json()["message"]
    allure.dynamic.title(case["用例编号"])


@allure.feature("admin:根据用户名或姓名分页获取用户列表")
@allure.link("/admin/list")
@pytest.mark.parametrize("case", list_param)
def test_login_param(case, get_evn, get_token, get_root_token):

    host = get_evn["host"]
    headers = get_evn["headers"]
    if case["用例标题"] == "没有相关权限":
        headers["Authorization"] = get_token
    else:
        headers["Authorization"] = get_root_token
    method=case["请求方法"]
    path = case["URL"]

    r = requests.request(method, url=host + path, headers=headers, json=case["请求体"])
    if "message" in r.json():
        assert r.json()["message"] == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])
