from abc import *


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def Iterator(self):
        pass


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def hasnext(self):
        pass

    @abstractmethod
    def next(self):
        pass

