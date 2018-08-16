# ######################################################
#
# http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html
#
# ListRemoveDuplicates.py
#
# Exercise 14
#
# ######################################################
#
# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.
#
# Extras:
#
# Write two different functions to do this - one using a loop and constructing a list, and another using sets.
# Go back and do Exercise 5 using sets, and write the solution for that in a different function.
#
# ######################################################

# Original Problem
import random


def generate_list():
    result_length = list(range(0, 99))
    result = random.sample(result_length, 10)
    result.sort()
    return result
    # return [1, 1, 2, 3, 4, 5, 5, 5, 6, 10]


a = generate_list()
print("Original list:      ", a)
a = sorted(list(set(a)))
print("Duplicates removed: ", a)
