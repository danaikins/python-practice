# ######################################################
#
# https://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html
#
# CheckPrimality.py
#
# Exercise 10
#
# ######################################################
#
# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity
# to practice using functions, described below.
#
# Discussion
#
# ######################################################

# Original Problem


def get_integer(text="Enter an Integer: "):
    return int(input(text))


def check_prime(user_input):
    list_divisors = find_divisors(user_input)
    number_is_prime = len(list_divisors)

    return number_is_prime == 0


def find_divisors(user_input):
    half_input = user_input // 2
    numbers = range(2, half_input + 1)
    answer = []
    for i in numbers:
        if user_input % i == 0:
            answer.append(i)
    return answer


user_number = get_integer("Enter a number to be checked for primality: ")
number_prime = check_prime(user_number)

if number_prime:
    print("The number \"{}\" is prime.".format(user_number))
else:
    print("The number \"{}\" is NOT prime.".format(user_number))
