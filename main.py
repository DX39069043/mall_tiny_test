# 开始测试
import pytest

if __name__ == '__main__':
    pytest.main(['--alluredir=./allure-results'])

# allure generate ./allure-results -o ./allure-report --clean