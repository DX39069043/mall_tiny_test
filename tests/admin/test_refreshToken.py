import allure
import pytest
from urllib3 import request

from utils.yaml_handler import YamlHandler

yamlhandler = YamlHandler("E:/code/python/mall_tiny_test/data/admin/refreshToken.yaml")
refreshToken_data = yamlhandler.read_yaml()


@allure.feature("admin:刷新token")
@allure.link("/admin/refreshToken")
@pytest.mark.parametrize("case", refreshToken_data)
def test_refreshToken(case, get_evn):
    host = get_evn["host"]
    path = case["URL"]
    method = case["请求方法"]
    headers = {**get_evn["headers"], **case["请求头"]}

    r = request(method, url=host + path, headers=headers)

    assert r.json()["message"] == case["预期结果"]
