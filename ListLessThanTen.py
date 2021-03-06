# ######################################################
#
# https://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
#
# ListLessThanTen.py
#
# Exercise 3
#
# ######################################################
#
# Take a list, say for example this one:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#
# and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
#
# 1.  Instead of printing the elements one by one, make a new list that has all the elements
#     less than 5 from this list in it and print out this new list.
# 2.  Write this in one line of Python.
# 3.  Ask the user for a number and return a list that contains only elements from the original
#     list a that are smaller than that number given by the user.
#
# ######################################################

# Original Problem
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for element in a:
    if element < 5:
        print(element)
print()

# Extra 1
b = []
for element in a:
    if element < 5:
        b.append(element)
print("{}\n".format(b))

# Extra 2
c = [element for element in a if int(element) < 5]
print("{}\n".format(c))

# Extra 3
user_input = int(input("Enter a number: "))
for element in a:
    if element < user_input:
        print(element)

