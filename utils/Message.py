import requests
import json
import time
import urllib
from urllib.parse import quote
import hashlib, base64, hmac

sec = "SEC0f79b8ea1e65cd996a233124448a2637"
web_hook = "https://yach-oapi.zhiyinlou.com/robot/send?access_token=SXlLcnBoblh0Zk9FM1ovMjhaeTZ2QWZMMk5rV2phYTZyU05obk8vNVlLazFvSHRZN2RaTlRVZHdBUW5IN21PdQ"
path_file = 'outputs/error.log'


class Message:
    def __init__(self, secret=sec, webhook=web_hook, path=path_file):
        self.secret = secret
        self.webhook = webhook
        self.path = path

    def get_url(self):
        timestamp = int(round(time.time() * 1000))
        secret_enc = bytes(self.secret.encode('utf-8'))
        string_to_sign = '{}\n{}'.format(timestamp, self.secret)
        string_to_sign_enc = bytes(string_to_sign.encode('utf-8'))
        hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
        sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
        post_url = self.webhook+"&timestamp=%s&sign=%s" % (timestamp, sign)  # 请求地址
        return post_url

    def get_recvlist(self, lines):
        recv_list = []
        for line in lines:
            line_list = line.split(" ")
            recv_item = line_list[1].split('@')[1][0:-2]
            print("recv_item------>", recv_item)
            recv_list.append(recv_item)
        print("recv_list------->", recv_list)
        return recv_list

    def send_message(self):
        with open(self.path) as fe:
            lines = fe.readlines()
            print(lines)
            count = len(lines)
            if count != 0:
                # 解析报错通知人
                recv_list = self.get_recvlist(lines)
                # 发送通知
                headers = {'Content-Type': 'application/json'}
                error_text = "本次执行共失败 " + str(count) + " 条\n" + "".join(lines)
                print(error_text)
                # 消息主体
                url = quote('http://jenkins-qa.xesv5.com/job/InterfaceAuto/allure/')
                single_url = "yach://yach.zhiyinlou.com/session/webview?url=%s" % url
                data = {
                    "msgtype": "markdown",
                    "markdown": {
                        "title": "接口自动化测试报警",
                        "text": "# 接口自动化测试报警\n ### %s\n  [点击查看报告详情](%s)" % (error_text, single_url)
                    },
                    "at": {'atWorkCodes': recv_list, 'isAtAll': False}
                }

                post_url = self.get_url()
                print(post_url)
                requests.post(post_url, data=json.dumps(data), headers=headers).json()
