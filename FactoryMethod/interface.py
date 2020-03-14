from abc import *


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def register_product(self, product):
        pass

    @abstractmethod
    def create_product(self, owner):
        pass

    def create(self, owner):
        product = self.create_product(owner)
        self.register_product(product)
        return product


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self):
        pass
