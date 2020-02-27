from Adapter.instance_case.interface import Time
from time import time


class GetTime:
    def __init__(self):
        self.unix_time = int(time())

    def get_now_unix_time(self):
        return self.unix_time


class GetTimeStr(Time):
    def __init__(self):
        self.ins = GetTime()

    def get_now_unix_time_str(self):
        return str(self.ins.get_now_unix_time())


if __name__ == '__main__':
    time = GetTimeStr()
    print(time.get_now_unix_time_str())
    print(type(time.get_now_unix_time_str()))

