# ######################################################
#
# http://www.practicepython.org/exercise/2014/07/05/18-cows-and-bulls.html
#
# CowsAndBulls.py
#
# Exercise 18
#
# ######################################################
#
# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
# a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell
# the user at the end.
#
# Say the number generated by the computer is 1038. An example interaction could look like this:
#
#   Welcome to the Cows and Bulls Game!
#   Enter a number:
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...
# Until the user guesses the number.
#
# ######################################################

# Original Problem
import random

if __name__ == "__main__":
    complete = False
    # answer = [1, 2, 3, 4]
    answer = [int(x) for x in str(random.randint(1000, 9999))]

    print("Answer: ", answer)
    while not complete:
        bulls = 0
        cows = 0
        user_input = int(input("Guess a number: "))
        user_list = [int(x) for x in str(user_input)]

        if user_list == answer:
            complete = True
            print("You Win!")
        else:
            for i in range(0, len(answer)):
                if answer[i] == user_list[i]:
                    cows = cows + 1
                else:
                    if user_list[i] in answer:
                        bulls = bulls + 1
        if not complete:
            print("{} cow, {} bull".format(cows, bulls))