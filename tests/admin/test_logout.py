import allure
import pytest
from requests import request

from utils.yaml_handler import YamlHandler

yamlhander = YamlHandler("E:/code/python/mall_tiny_test/data/admin/logout.yaml")
logout_data = yamlhander.read_yaml()

@allure.feature("admin:用户登出")
@allure.link("/admin/link")
@pytest.mark.parametrize("case",logout_data)
def test_logout(case, get_evn, get_root_token):

    host=get_evn["host"]
    path=case["URL"]
    headers=get_evn["headers"]
    headers["Authorization"]=get_root_token
    method=case["请求方法"]

    r=request(method=method,url=host+path,headers=headers)
    assert r.json()["message"]==case["预期结果"]
    allure.dynamic.title(case["用例编号"])