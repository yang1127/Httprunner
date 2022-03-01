import os
import time

if __name__=="__main__":

    # 执行case
    # cmd = 'sudo /home/dev/webuienv/bin/pytest  ./testcases --clean-alluredir  --alluredir=results'
    # os.system(cmd)

    # 判断是否有错误case，有则发送报警邮件
    # 等报告生成完成
    # time.sleep(5)

    # cmd = ''' cat allure-report/data/suites.csv | grep -v passed | grep -v Status  | awk -F ',' '{print $1,$10}' > logs/error.log'''
    # os.system(cmd)

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
        cmd = 'pytest testcases --alluredir reports'
        os.system(cmd)
        cmd = 'allure generate reports -o results --clean'
        os.system(cmd)