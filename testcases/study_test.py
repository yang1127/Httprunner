# NOTE: Generated By HttpRunner v3.1.5
# FROM: har\search.har
# 参数化驱动

import pytest
from httprunner import HttpRunner, Config, Step, RunRequest, Parameters
from config.ExcelUtiltest import ParseExcel

'''
class TestCaseSearch(HttpRunner):
    # 法一：列表 —— 直接指定参数列表（笛卡尔积）
    @pytest.mark.parametrize('parma', Parameters({"city": ["西安", "临潼"]}))
    def test_start(self, parma):
        super().test_start(parma)

    config = Config("测试测试～").verify(False)

    teststeps = [
        Step(
            RunRequest("yzq测试")
                .post("https://api.vvhan.com/api/weather?")
                .with_headers(
                **{
                    "User-Agent": "python-requests/2.27.1",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "HRUN-Request-ID": "HRUN-a70728d8-dd82-4065-9f54-92f0e7610827-414571",
                    "Content-Length": "0"
                }
            )
                .with_params(
                **{
                    "city": "$city",
                    "type": "week"
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
    ]
'''

'''
class TestCaseSearch(HttpRunner):
    # 法二：debugtalk.py 回调
    @pytest.mark.parametrize('parma', Parameters({"city": '${get_city()}'}))
    def test_start(self, parma):
        super().test_start(parma)

    config = Config("测试测试～").verify(False)

    teststeps = [
        Step(
            RunRequest("yzq测试")
                .post("https://api.vvhan.com/api/weather?")
                .with_headers(
                **{
                    "User-Agent": "python-requests/2.27.1",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "HRUN-Request-ID": "HRUN-a70728d8-dd82-4065-9f54-92f0e7610827-414571",
                    "Content-Length": "0"
                }
            )
                .with_params(
                **{
                    "city": "$city",
                    "type": "week"
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
    ]
'''

'''
class TestCaseSearch(HttpRunner):
    # 法三：Parameterize类的回调，例如csv：${parameterize(account.csv)}
    @pytest.mark.parametrize('param', Parameters({"city": '${parameterize(testdata/data.csv)}'}))
    def test_start(self, param):
        super().test_start(param)

    config = Config("测试测试～").verify(False)

    teststeps = [
        Step(
            RunRequest("yzq测试")
                .post("https://api.vvhan.com/api/weather?")
                .with_headers(
                **{
                    "User-Agent": "python-requests/2.27.1",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "HRUN-Request-ID": "HRUN-a70728d8-dd82-4065-9f54-92f0e7610827-414571",
                    "Content-Length": "0"
                }
            )
                .with_params(
                **{
                    "city": "$city",
                    "type": "week"
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
    ]
'''


class TestCaseSearch(HttpRunner):
    # 法三：xlsx文件
    data = ParseExcel('/Users/yangzhiqi/HPtest/testdata/exceldata.xlsx', 'Sheet1')
    datalist = data.getDatasFromSheet()  # 调取getDatasFromSheet()函数，读取excel数据

    @pytest.mark.parametrize('param', Parameters({"city": datalist}))
    def test_start(self, param):
        super().test_start(param)

    config = Config("测试测试～").verify(False)

    teststeps = [
        Step(
            RunRequest("yzq测试")
                .post("https://api.vvhan.com/api/weather?")
                .with_headers(
                **{
                    "User-Agent": "python-requests/2.27.1",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept": "*/*",
                    "Connection": "keep-alive",
                    "HRUN-Request-ID": "HRUN-a70728d8-dd82-4065-9f54-92f0e7610827-414571",
                    "Content-Length": "0"
                }
            )
                .with_params(
                **{
                    "city": "$city",
                    "type": "week"
                }
            )
                .validate()
                .assert_equal("status_code", 200)
        ),
    ]


if __name__ == '__main__':
    TestCaseSearch().test_start()

