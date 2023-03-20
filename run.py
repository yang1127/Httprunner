import os

from utils.Message import Message


def env_clear():
        path = os.getcwd()
        if os.path.exists(path + "/results"):
            os.system("rm -rf results")
        if os.path.exists(path + "/reports"):
            os.system("rm -rf reports")


if __name__ == "__main__":
        # 清除上次报告
        env_clear()

        # 执行case
        cmd = 'pytest testcases --alluredir results'
        os.system(cmd)
        cmd = 'allure generate results -o reports --clean'
        os.system(cmd)

        # 发送消息
        Message().send_message()


