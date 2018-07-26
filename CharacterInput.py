# ######################################################
#
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html
#
# CharacterInput.py
#
# ######################################################
#
# Create a program that asks the user to enter their name and their age. Print out a message addressed to
# them that tells them the year that they will turn 100 years old.
#
# Extras:
#
# 1. Add on to the previous program by asking the user for another number and printing out that many copies of the
#    previous message. (Hint: order of operations exists in Python)
# 2. Print out that many copies of the previous message on separate lines.
#    (Hint: the string "\n is the same as pressing the ENTER button)
#
# ######################################################

from datetime import datetime

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_number = int(input("Enter your favorite number: "))

current_year = datetime.now().year
age_100_years = (100 - user_age) + current_year

print("Hi {}. You will turn 100 in year {}\n".format(user_name, age_100_years) * user_number)
