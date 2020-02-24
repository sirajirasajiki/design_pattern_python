from interface import *


class Subject(Aggregate):
    students = list()
    last = int()

    def __init__(self):
        self.last = 0

    def get_student(self, index):
        return self.students[index]

    def add_student(self, student):
        self.students.append(student)
        self.last = self.last + 1

    def get_number_of_students(self):
        return self.last

    @classmethod
    def iterator(self):
        return SubjectIterator()


class SubjectIterator(Iterator):
    subject = Subject()
    index = int()

    def __init__(self):
        self.index = 0

    @classmethod
    def has_next(cls):
        if cls.index < cls.subject.get_number_of_students():
            return True

        return False

    @classmethod
    def next(cls):
        student = cls.subject.get_student(cls.index)
        cls.index = cls.index + 1
        return student


if __name__ == '__main__':
    ss = Subject()
    ss.add_student('tt')
    tt = ss.iterator()
    print(tt.next())

