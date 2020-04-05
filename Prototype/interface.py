from abc import *
import copy


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, st):
        pass

    @abstractmethod
    def create_clone(self):
        pass
