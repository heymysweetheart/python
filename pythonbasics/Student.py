__author__ = 'yuliang'

'''This is a python class'''

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('{0} has been born'.format(self.name))

s1 = Student('leo', 25)  #output: leo has been born
