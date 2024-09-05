# 开始测试
import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir=./allure-results'])

# allure generate ./allure-results -o ./allure-report --clean


# bug:把用户:admin改回超级管理员（现在是商品管理员）；后台数据库直接改
