# 获取当前登陆用户信息
import allure
import pytest
from pytest_order.plugin import pytest_generate_tests
from requests import request

from utils.yaml_handler import YamlHandler

yamlhander = YamlHandler("E:/code/python/mall_tiny_test/data/admin/info.yaml")
info = yamlhander.read_yaml()

yamlhander_token = YamlHandler("E:/code/python/mall_tiny_test/data/admin/token.yaml")
raw_token = yamlhander_token.read_yaml()
token = raw_token["tokenHead"] + raw_token["token"]


@allure.feature("admin:获取当前登录用户的信息")
@allure.link("/admin/info")
@pytest.mark.parametrize("case", info)
def test_info(case, get_evn):
    host = get_evn["host"]
    headers = get_evn["headers"]
    headers["Authorization"] = token
    path = case["URL"]
    method=case["请求方法"]

    r = request(method, url=host + path, headers=headers)
    assert r.json() == case["预期结果"]
    allure.dynamic.title(case["用例编号"])

