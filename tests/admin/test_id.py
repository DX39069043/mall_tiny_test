import allure
import pytest
from requests import request

from conftest import get_token
from utils.yaml_handler import YamlHandler

yamlhander_data = YamlHandler("E:/code/python/mall_tiny_test/data/admin/id_data.yaml")
id_data = yamlhander_data.read_yaml()

@allure.link("/admin/{id}")
@allure.feature("admin:获取指定用户信息")
@pytest.mark.parametrize("case", id_data)
def test_id_data(case, get_evn, get_root_token, get_token):

    host = get_evn["host"]
    path = case["URL"]
    method = case["请求方法"]
    headers = get_evn["headers"]
    if case["用例标题"] == "没有相关权限":
        headers["Authorization"] = get_token
    else:
        headers["Authorization"] = get_root_token

    r = request(method, url=host + path, headers=headers)
    if "message" in r.json():
        assert r.json() == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])


yamlhander_param=YamlHandler("E:/code/python/mall_tiny_test/data/admin/id_param.yaml")
id_param=yamlhander_param.read_yaml()

@allure.link("/admin/{id}")
@allure.feature("admin:获取指定用户信息")
@pytest.mark.parametrize("case", id_param)
def test_id_param(case,get_evn,get_token,get_root_token):

    host = get_evn["host"]
    path = case["URL"]
    method = case["请求方法"]
    headers = get_evn["headers"]
    if case["用例标题"] == "没有相关权限":
        headers["Authorization"] = get_token
    else:
        headers["Authorization"] = get_root_token

    r = request(method, url=host + path, headers=headers)
    if "message" in r.json():
        assert r.json() == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])