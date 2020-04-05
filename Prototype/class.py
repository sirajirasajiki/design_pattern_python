from Prototype.interface import *
import copy


class Manager:
    def __init__(self):
        self.__showcase = dict()

    def register(self, name, proto):
        self.__showcase[name] = proto

    def create(self, pname):
        # JavaではクラスキャストできるのでProductを継承できます。
        # PythonではクラスキャストできないのでProductを継承できないです。
        # なのでdeepcopyでオブジェクトのコピーをしています。
        p = self.__showcase[pname]
        return copy.deepcopy(p)


class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s):
        length = len(s)
        line = self.decochar * (length + 4)
        print(line)
        print(self.decochar + ' ' + s + ' ' + self.decochar)
        print(line)
        print('')

    def create_clone(self):
        p = copy.deepcopy(self)
        return p


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s):
        length = len(s)
        line = self.ulchar * (length + 2)
        print('"' + s + '"')
        print(line)
        print('')

    def create_clone(self):
        p = copy.deepcopy(self)
        return p


if __name__ == '__main__':
    manager = Manager()
    mbox = MessageBox('*')
    upen = UnderlinePen('-')
    manager.register('warning', mbox)
    manager.register('strong', upen)
    pa = manager.create('warning')
    pb = manager.create('strong')

    pa.use('test')
    pb.use('neet')
