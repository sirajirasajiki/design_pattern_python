from abc import *


class Mahjong(metaclass=ABCMeta):
    __mahjong = None
    __score = [25000] * 4

    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        else:
            cls._instance.input = input

        return cls._instance

    @classmethod
    def get_score(cls):
        return cls.__score

    @classmethod
    def score_calculation(cls, add_list):
        """
        点数の計算を行う。
        減るときは-とする
        :param add_list:計算リスト
        """
        cls.__score = [a + b for a, b in zip(cls.__score, add_list)]


if __name__ == '__main__':
    a = Mahjong().get_instance()
    b = Mahjong().get_instance()
    if a is b:
        print('同じオブジェクト')
    else:
        print('異なるオブジェクト')

    print(a.get_score())
    a.score_calculation([0,8000, -8000, 0])
    print(a.get_score())
    print(b.get_score())
