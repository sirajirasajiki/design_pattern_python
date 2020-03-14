from FactoryMethod.interface import *


class PCFactory(Factory):
    def __init__(self):
        self._owners = list()

    def register_product(self, product):
        self._owners.append(product.get_owner())

    def create_product(self, owner):
        return PCProduct(owner)

    def get_owners(self):
        return self._owners


class PCProduct(Product):
    def __init__(self, owner):
        self._owner = owner

    def use(self):
        print('{0}さんのPCを使います。'.format(self._owner))

    def get_owner(self):
        return self._owner


if __name__ == '__main__':
    factory = PCFactory()
    product1 = factory.create('sirajira')
    product1.use()
    print(factory.get_owners())
    product2 = factory.create('sajiki')
    product2.use()
    print(factory.get_owners())
