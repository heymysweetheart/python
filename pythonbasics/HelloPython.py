
__author__ = 'leo'
import os
import sys
import random

quote = "\"Always remember you are unique"
multi_line_quote = '''just like
everyone
else'''

print("%s %s %s" %('I like the quote', quote, multi_line_quote))

print("\n" * 5)

print("I don't like this", end="")
print(" new lines")

#tuple

pi_tuple = (3,1,4,5,9)
print(pi_tuple)

# pi_list = list(tuple)
print(max(pi_tuple))
print(len(pi_tuple))
print("min of the tuple: ",min(pi_tuple))

num_range = range(1,19)

for num in num_range:
    print("num is: ", num)


fruit = ["apple", "pear", "branans", "peach"]
for a in fruit:
    print(a, ' ', end="")
print("\n")
print(max(fruit))

print("what is your name?")
name = sys.stdin.readline()
print(name)

#a function that return a tuple
A = random.randint(1,6)
B = random.randint(1,6)
print("A= ", A)
print("B= ", B)
def make_them_different(a, b):
    while a==b:
        a = random.randint(1,6)
        b = random.randint(1,6)
    return (a, b)
new_A, new_B = make_them_different(A, B)
print("new_A=", new_A)
print("new_B=", new_B)

print(make_them_different(3,3))

#files
test_file = open("test.txt", "wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file", "UTF-8"))
test_file.close()

file_for_read = open("test.txt", "r+")
text_in_file = file_for_read.read()
print(text_in_file)

os.remove("test.txt")

#python class
class Animal:
    __name = None
    __height= 0
    __weight= 0
    __sound= 0

    def __init__(self, name, height, weight, sound):
        self.__name = name
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return  self.__name

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return  self.__height

    def set_weight(self, weight):
        self.__weight = weight

    def get_weight(self):
        return  self.__weight

    def set_sound(self, sound):
        self.__sound = sound

    def get_sound(self):
        return  self.__sound

    def get_type(self):
        print("Animal")

    def toString(self):
        return "{} is {} cm tall and {} kg weight and say {} .".format(self.get_name(),
                                                                    self.get_height(),
                                                                    self.get_weight(),
                                                                    self.get_sound())

# initialization of the class
cat = Animal("tom", 10, 2, "meow")
print(cat.toString())
print(cat.get_height())

# inheritage
class Dog(Animal):
    __owner = ""

    def __init__(self, name, height, weight, sound, owner):
        self.__owner = owner
        super(Dog, self).__init__(name, height, weight, sound)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.get_owner()

    def get_type(self):
        print("Dog")

    def multi_sound(self, sound_time = None):
        if(sound_time == 0):
            print(self.get_sound())
        else:
            print(self.get_sound() * sound_time)

spot = Dog("hero", 12, 20, "wang", "leo")
print(spot.toString())
# print(spot.get_type())

class AnimalTest:
    def get_type(self, animal):
        return animal.get_type()

test_animals= AnimalTest()
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multi_sound(4)