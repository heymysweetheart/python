
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