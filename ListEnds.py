# ######################################################
#
# https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
#
# ListEnds.py
#
# Exercise 12
#
# ######################################################
#
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
# the first and last elements of the given list. For practice, write this code inside a function.
#
# ######################################################

# Original Problem
import random


def make_list(current_list):
    result = [current_list[0], current_list[-1]]
    return result


def generate_list():
    a_length = random.randint(10, 20)
    result = random.sample(range(1, 99), a_length)
    return result


a = generate_list()
print(a)
new_list = make_list(a)
print(new_list)
