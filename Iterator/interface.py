from abc import *


class Aggregate(metaclass=ABCMeta):
    @abstractmethod
    def iterator(self):
        pass


class Iterator(metaclass=ABCMeta):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

