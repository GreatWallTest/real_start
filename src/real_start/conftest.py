from datetime import datetime
import pytest



result_date = {
        "passed":0,
        "failed":0
}
def pytest_configure():
        start = datetime.now()
        print(start)


def pytest_unconfigure():
        end = datetime.now()
        print(end)
