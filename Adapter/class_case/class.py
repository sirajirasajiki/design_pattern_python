from Adapter.class_case.interface import Time
from time import time


class GetTime:
    def __init__(self):
        self.unix_time = int(time())

    def get_now_unix_time(self):
        return self.unix_time


class GetTimeStr(GetTime, Time):

    def __init__(self):
        super().__init__()

    def get_now_unix_time_str(self):
        return str(super().get_now_unix_time())


if __name__ == '__main__':
    time = GetTimeStr()
    print(time.get_now_unix_time_str())
    print(type(time.get_now_unix_time_str()))

    # クラスを継承しているのでそのままint型でも取得できます。
    print(time.get_now_unix_time())
    print(type(time.get_now_unix_time()))
