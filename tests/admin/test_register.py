# 用户注册
import allure
import pytest
import requests

from utils import yaml_handler

yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/register.yaml")
register_data = yamlhandler.read_yaml()["data"]
register_param = yamlhandler.read_yaml()["param"]


@allure.feature("admin:用户注册")
@allure.link("/admin/register")
@pytest.mark.parametrize("case", register_data)
def test_register_data(case, get_evn):

    host = get_evn["host"]
    headers = {**get_evn["headers"],**case["请求头"]}
    path = case["URL"]
    method=case["请求方法"]

    r = requests.request(method, url=host + path, headers=headers, json=case["请求体"])
    assert r.json()["message"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])


@allure.feature("admin:用户注册")
@allure.link("/admin/register")
@pytest.mark.parametrize("case", register_param)
def test_register_param(case, get_evn):

    host = get_evn["host"]
    headers = {**get_evn["headers"],**case["请求头"]}
    method=case["请求方法"]
    path = case["URL"]

    r = requests.request(method, url=host + path, headers=headers, json=case["请求体"])
    if "message" in r.json():
        assert r.json()["message"] == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])
