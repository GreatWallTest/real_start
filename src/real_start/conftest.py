from datetime import datetime
import pytest

def pytest_configure():
        start = datetime.now()
        print(start)


def pytest_unconfigure():
        end = datetime.now()
        print(end)