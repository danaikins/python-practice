# ######################################################
#
# http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#
# PasswordGenerator.py
#
# Exercise 16
#
# ######################################################
#
# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a
# mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating
# a new password every time the user asks for a new password. Include your run-time code in a main method.
#
# Extra:
#
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
#
# ######################################################

# Original Problem
import string
import random

password_complexity = int(input("How many digits should your password be? "))

characters_available = string.ascii_letters + string.digits + "~!@#$%^&*()_+-=`[]\{}|;':\",./<>?"
print(characters_available)

# for i in range(1, 11):
password = "".join(random.sample(characters_available, password_complexity))
print(password)
