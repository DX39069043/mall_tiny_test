import allure
import pytest
import requests
from requests import request

from conftest import get_root_token
from tests.admin.test_role_update import yamlhander_data
from utils import yaml_handler

yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/data/admin/updatePassword.yaml")
updatePassword_data = yamlhandler.read_yaml()["data"]
updatePassword_param=yamlhandler.read_yaml()["param"]

@allure.feature("admin:修改指定用户密码")
@allure.link("/admin/updatePassword")
@pytest.mark.parametrize("case", updatePassword_data)
def test_updatePassword_date(case,get_evn,get_token,get_root_token):

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
    # 把密码恢复为原来的密码
    if case["用例标题"]!="没有相关权限":
        data={
            "username":"123456",
            "password":"123456"
        }
        r0 = request(method="POST",url=host+"/admin/update/16",headers=headers,json=data)

@allure.feature("admin:修改指定用户密码")
@allure.link("/admin/updatePassword")
@pytest.mark.parametrize("case", updatePassword_param)
def test_updatePassword_param(case,get_evn,get_token,get_root_token):

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
    # 把密码恢复为原来的密码
    if case["用例标题"]!="没有相关权限":
        data={
            "username":"123456",
            "password":"123456"
        }
        r0 = request(method="POST",url=host+"/admin/update/16",headers=headers,json=data)
