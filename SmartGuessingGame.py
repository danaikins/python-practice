print("Guessing Game! Enter a range of numbers, then think of a number for the computer to guess.")
low_number = int(input("Enter the low number: "))
high_number = int(input("Enter the high number: "))
guess_count = 0

while True:
    computer_guess = (low_number + high_number) // 2
    print("Computer guesses {}".format(computer_guess))
    guess_count += 1

    guess_right = input("Yes, higher, or lower? (y/h/l): ")
    if guess_right == 'y':
        print("Computer wins in {} guesses!".format(guess_count))
        break
    elif guess_right == 'h':
        low_number = computer_guess + 1
    elif guess_right == 'l':
        high_number = computer_guess - 1
