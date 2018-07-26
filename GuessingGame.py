from random import randint

# Guessing game 1-20
low_guess = 1
high_guess = 20

print("Guessing game, think of a number from 1-20. Computer will guess.")

while True:
    computer_guess = randint(low_guess, high_guess)
    yes_no = None
    user_input = ""

    yes_no = input("Computer guesses: {}. (y/n): ".format(computer_guess))
    if yes_no == 'y':
        print("You Lose!")
        break

    user_input = input("Higher or Lower? (h/l): ")
    if user_input == 'h':
        low_guess = computer_guess + 1
    elif user_input == 'l':
        high_guess = computer_guess - 1
    else:
        print("Error")
        break
