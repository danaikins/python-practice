# ######################################################
#
# https://www.practicepython.org/exercise/2014/11/11/20-element-search.html
#
# ElementSearch.py
#
# Exercise 20
#
# ######################################################
#
# Write a function that takes an ordered list of numbers (a list where the elements are in order from
# smallest to largest) and another number. The function decides whether or not the given number is inside
# the list and returns (then prints) an appropriate boolean.
#
# Extras:
#
# Use binary search.
#
# ######################################################


def number_in_list(user_list, number):
    return number in user_list


def binary_search(user_list, number):
    solved = False
    list_length = int(len(user_list))
    index = list_length // 2

    while not solved:
        if user_list[index] == number:
            solved = True


if __name__ == "__main__":
    a = [1, 3, 5, 30, 42, 43, 500]
    print("List: ", a)
    user_input = int(input("Enter a number to search for: "))
    result = number_in_list(a, user_input)

    if result:
        print("{} is in the list!".format(user_input))
    else:
        print("{} is NOT in the list.".format(user_input))
