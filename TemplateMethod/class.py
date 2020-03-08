from TemplateMethod.interface import *


class CharDisplay(AbstractDisplay):

    def __init__(self, ch):
        self.ch = ch

    def open(self):
        print('<<', end='')

    def print(self):
        print(self.ch, end='')

    def close(self):
        print('>>')


class StringDisplay(AbstractDisplay):
    def __init__(self, ch):
        self.ch = ch

    def _printline(self):
        for i in range(10):
            print('-', end='')
        print('')

    def open(self):
        self._printline()

    def print(self):
        print(self.ch)

    def close(self):
        self._printline()


if __name__ == '__main__':
  cd = CharDisplay('test')
  cd.display()
  sd = StringDisplay('test')
  sd.display()
