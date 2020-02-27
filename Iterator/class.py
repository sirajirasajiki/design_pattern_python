from Iterator.interface import *


class Subject(Aggregate):

    def __init__(self):
        self.students = list()
        self.last = 0

    def get_student(self, index):
        return self.students[index]

    def add_student(self, student):
        self.students.append(student)
        self.last = self.last + 1

    def get_number_of_students(self):
        return self.last

    def iterator(self):
        return SubjectIterator(self)


class SubjectIterator(Iterator):
    def __init__(self, sub):
        self.subject = sub
        self.index = 0

    def has_next(self):
        if self.index < self.subject.get_number_of_students():
            return True

        return False

    def next(self):
        stu = self.subject.get_student(self.index)
        self.index = self.index + 1
        return stu


class Student():
    name = int()
    student_number = int()

    def __init__(self, name, number):
        self.name = name
        self.student_number = number


if __name__ == '__main__':
    student = Student('Sirajira Sajiki', 1)
    student2 = Student('Sirajira Sajiki2', 2)
    subject = Subject()
    subject.add_student(student)
    subject.add_student(student2)
    print(subject.last)
    iterator = subject.iterator()
    print(iterator.has_next())
    while iterator.has_next():
        next = iterator.next()
        print(next.name)
        print(next.student_number)
