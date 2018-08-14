# ######################################################
#
# https://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html
#
# Fibonacci.py
#
# Exercise 13
#
# ######################################################
#
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this
# opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers
# in the sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence.
#
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
#
# ######################################################

# Original Problem
num_iterations = int(input("Enter an integer for # of fibonacci sequence: "))
num_one: int = 0
num_two: int = 1
num_temp: int = 0
full_list = []

for x in range(0, num_iterations):
    full_list.append(num_temp)
    num_temp = num_two
    num_two = num_one + num_two
    num_one = num_temp

print(full_list)
