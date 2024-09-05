import pymysql
import pytest

from utils import yaml_handler
from utils.yaml_handler import YamlHandler


@pytest.fixture(scope="session")
def get_evn():
    yamlhandler = yaml_handler.YamlHandler("E:/code/python/mall_tiny_test/config/env.yaml")
    evn_config = yamlhandler.read_yaml()
    return evn_config

# 连接数据库
@pytest.fixture(scope="session")
def db_connection():

    # 利用工具类读取数据库参数
    yamlhandler = yaml_handler.YamlHandler("/config/database.yaml")
    dbconfig = yamlhandler.read_yaml()

    # 连接到数据库
    connection = pymysql.connect(
        host=dbconfig["host"],
        user=dbconfig["user"],
        password=dbconfig["password"],
        database=dbconfig["database"]
    )
    return connection

# 关闭数据库连接
@pytest.fixture(scope="session")
def db_close(connection):
    connection.cursor.close()
    connection.close()

# 提取root令牌token
@pytest.fixture(scope="session")
def get_root_token():
    yamlhander_token = YamlHandler("E:/code/python/mall_tiny_test/data/admin/token.yaml")
    raw_token = yamlhander_token.read_yaml()[0]
    token = raw_token["tokenHead"] + raw_token["token"]
    return token

# 提取非root令牌token
@pytest.fixture(scope="session")
def get_token():
    yamlhander_token = YamlHandler("E:/code/python/mall_tiny_test/data/admin/token.yaml")
    raw_token = yamlhander_token.read_yaml()[1]
    token = raw_token["tokenHead"] + raw_token["token"]
    return token
