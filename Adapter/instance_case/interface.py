from abc import *


class Time(metaclass=ABCMeta):
    @abstractmethod
    def get_now_unix_time_str(self):
        pass
