# ######################################################
#
# https://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
#
# RockPaperScissors.py
#
# Exercise 8
#
# ######################################################
#
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner, and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock
#
# ######################################################

# Original Problem
print("Rock, Paper, Scissors!")

player1_input = input("Player 1, rock paper scissors, or quit?").lower()
player2_input = input("Player 2, rock paper scissors, or quit?").lower()
while player1_input != "quit" and player2_input != "quit":
    if player1_input == player2_input:
        print("You tie!")
    elif player1_input == "rock":
        if player2_input == "paper":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    elif player1_input == "paper":
        if player2_input == "rock":
            print("Player 1 wins!")
        else:
            print("Player 2 wins!")
    elif player1_input == "scissors":
        if player2_input == "rock":
            print("Player 2 wins!")
        else:
            print("Player 1 wins!")
    else:
        print("INCORRECT INPUT!")
        print("WOMP WOMP")

    player1_input = input("Player 1, rock paper scissors, or quit?").lower()
    player2_input = input("Player 2, rock paper scissors, or quit?").lower()
