import requests

from utils.yaml_handler import YamlHandler


class TestAdminLoginToken():
    def test_admin_login_token(self):
        host = "http://localhost:8080"
        path = "/admin/login"
        data = {
            "username":"admin",
            "password":"macro123"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
            "Content_Type":"application/json"
        }
        r = requests.request("POST", url=host + path, headers=headers, json=data)
        response = r.json()
        yamlHander = YamlHandler("E:/code/python/mall_tiny_test/data/token.yaml")
        # 将得到的token和tokneHead存入yaml文件
        yamlHander.write_yaml(response["data"])
        print(response)