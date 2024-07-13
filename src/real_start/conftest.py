from datetime import datetime, timedelta
import pytest
import requests, json


result_date = {
        "passed": 0,
        "failed": 0,
        "start": ...,
        "api": ...,
        "during": ...,
        "end": ...
}
def pytest_configure(config: pytest.Config):
        result_date["start"] = datetime.now()
        result_date["api"] = config.getini("send_api")
        # print("这是钉钉api", result_date["api"])
        
def pytest_unconfigure():

        result_date["end"] = datetime.now()

        result_date["during"] = (result_date["end"] - result_date["start"]).total_seconds()
        rate = (result_date["passed"] / (int(result_date["passed"]) + int(result_date["failed"]))) * 100
        mes_data = f"""通过率：{rate}%
测试开始时间：{result_date["start"].strftime("%Y-%m-%d %H:%M:%S")}
测试用例数量：{int(result_date["passed"]) + int(result_date["failed"])}
测试用时：{result_date["during"]}s
通过数量：{result_date["passed"]}
失败数量：{result_date["failed"]}
"""
        send(mes_data)


def send(mes_data):
        head = {"content-type": "application/json"}
        date = {
          "msgtype": "text",
          "text": {
            "content": mes_data
          },
          "at": {
            "isAtAll": True,
            "atMobiles": []
          }
        }
        res = requests.post(url=result_date["api"], headers=head, data=json.dumps(date))
        print(res.text)

def pytest_addoption(parser):
    parser.addini("send_api", help="钉钉发送消息地址")


def pytest_report_teststatus(report):
    if report.when == "call":
        result_date[report.outcome] += 1
