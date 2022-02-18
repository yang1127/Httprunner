import time

from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


# 数据驱动，debugtalk.py 回调
def get_city():
    return[
        {'city': '西安'},
        {'city': '临潼'}
    ]



