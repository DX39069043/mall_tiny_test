import allure
import pytest
import requests

from conftest import get_root_token
from utils import yaml_handler

yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/update.yaml")
update_data = yamlhandler.read_yaml()["data"]
update_param = yamlhandler.read_yaml()["param"]

@allure.feature("admin:修改指定用户信息")
@allure.link("/admin/update")
@pytest.mark.parametrize("case", update_data)
def test_update_date(case,get_evn,get_token,get_root_token):

    host = get_evn["host"]
    headers = {**get_evn["headers"],**case["请求头"]}
    if case["用例标题"]=="没有相关权限":
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


@allure.feature("admin:修改指定用户信息")
@allure.link("/admin/update")
@pytest.mark.parametrize("case", update_param)
def test_update_param(case,get_evn,get_root_token):

    host = get_evn["host"]
    headers = {**get_evn["headers"],**case["请求头"]}
    headers["Authorization"] = get_root_token
    method=case["请求方法"]
    path = case["URL"]

    r = requests.request(method, url=host + path, headers=headers, json=case["请求体"])
    if "message" in r.json():
        assert r.json()["message"] == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])