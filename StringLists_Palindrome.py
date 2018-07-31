# ######################################################
#
# https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html
#
# StringLists_Palindrome.py
#
# Exercise 6
#
# ######################################################
#
# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)
#
# ######################################################

# Original Problem
user_input = input("Enter a string for palindrome testing: ")
begin = user_input[0:len(user_input) // 2]
word_end = user_input[:len(user_input) // 2:-1]

if begin == word_end:
    print("{} is a palindrome!".format(user_input))
else:
    print("{} is not a palindrome.".format(user_input))

if user_input[::1] == user_input[::-1]:
    print("Palindrome!")
