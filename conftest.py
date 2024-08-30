import pymysql
import pytest

from utils import yaml_handler


@pytest.fixture()
def db_connection():

    # 利用工具类读取数据库参数
    yamlhandler = yaml_handler.YamlHandler("E:\code\python\mall_tiny_test\config\database_config.yaml")
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
@pytest.fixture()
def db_close(connection):
    connection.cursor.close()
    connection.close()
