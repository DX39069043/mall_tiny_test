import allure
import pytest
from requests import request

from conftest import get_token
from utils.yaml_handler import YamlHandler

yamlhander_data = YamlHandler("E:/code/python/mall_tiny_test/data/admin/role_data.yaml")
role_data = yamlhander_data.read_yaml()

@allure.link("/admin/role")
@allure.feature("admin:获取指定用户的角色")
@pytest.mark.parametrize("case", role_data)
def test_role_update_data(case, get_evn, get_root_token, get_token):

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
        assert r.json()["message"] == case["预期结果"]
    else:
        assert r.json()["error"] == case["预期结果"]
    allure.dynamic.title(case["用例编号"])