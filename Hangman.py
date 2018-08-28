secret_word = "HANGMAN"
guess_count = 0
correct_letters = [None]
incorrect_letters = [None]
answer = []

answer_length = 0
current_length = 0
num_correct_guesses = 0
num_incorrect_guesses = 0
num_total_guesses = 0


def init():
    global correct_letters, answer, answer_length

    print("Welcome to HANGMAN!")
    user_word = str(input("Enter your word for Player 2 to guess: ")).upper()

    answer = list(user_word)
    answer_length = len(answer)
    correct_letters = list("_" * answer_length)
    incorrect_letters.clear()

    return user_word


def main_loop():
    global correct_letters, answer_length, current_length, num_correct_guesses, num_incorrect_guesses, num_total_guesses

    while answer_length != current_length:
        guess_again = True
        while guess_again:
            current_guess = str(input("Enter a letter: ")).upper()
            if len(current_guess) == 1 and ((current_guess >= "A") and (current_guess <= "Z")):
                guess_again = False

        if contains_letter(current_guess):
            locations = ([pos for pos, char in enumerate(secret_word) if char == current_guess])

            for l in locations:
                correct_letters[int(l)] = current_guess
                current_length += 1
            num_correct_guesses += 1
        else:
            incorrect_letters.extend(current_guess)
            num_incorrect_guesses += 1
        num_total_guesses += 1
        print_hangman()


def contains_letter(letter):
    if letter in secret_word:
        return True
    else:
        return False


def print_hangman():
    global correct_letters, incorrect_letters
    global answer_length, current_length
    temp_str = ""

    for c in correct_letters:
        temp_str = temp_str + c + " "

    print("Incorrect: ", incorrect_letters)
    print("Correct: ", temp_str)
    print("Correct Guesses: {}\nIncorrect guesses: {}\nTotal Guesses: {}".format(num_correct_guesses, num_incorrect_guesses, num_total_guesses ))


if __name__ == "__main__":
    secret_word = init()
    main_loop()
