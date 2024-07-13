from datetime import datetime
import pytest
import requests, json


result_date = {
        "passed":0,
        "failed":0
}
def pytest_configure(config: pytest.Config):
        result_date["start"] = datetime.now()
        result_date["api"] = config.getini("send_api")
        # print("这是钉钉api", result_date["api"])
        
def pytest_unconfigure():
        result_date["end"] = datetime.now()

        result_date["during"] = result_date["end"] - result_date["start"]


        url = "https://oapi.dingtalk.com/robot/send?access_token=6deb48ff96240e5e55d8d081ab4cb551fffa8169c924cbd472bac6c81edbc40d"
        head = {"content-type": "application/json"}
        date = {
          "msgtype": "text",
          "text": {
            "content": "这是一条测试消息\n"
          },
          "at": {
            "isAtAll": True,
            "atMobiles": []
          }
        }
        res = requests.post(url, headers=head, data=json.dumps(date))
        print(res.text)

def pytest_addoption(parser):
    parser.addini(
        "send_api",
        help="钉钉发送消息地址"
    )