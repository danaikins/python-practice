# ######################################################
#
# https://www.practicepython.org/exercise/2014/02/26/04-divisors.html
#
# Divisors.py
#
# Exercise 4
#
# ######################################################
#
# Create a program that asks the user for a number and then prints out a list of all the
# divisors of that number. (If you don’t know what a divisor is, it is a number that divides
# evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
#
# ######################################################

# Original Problem
print("This program lists all divisors of a user entered number")
user_input = int(input("Enter a number: "))

half_input = user_input // 2
numbers = range(2, half_input+1)
print(numbers)

answer = []
for i in numbers:
    if user_input % i == 0:
        answer.append(i)

print(answer)
