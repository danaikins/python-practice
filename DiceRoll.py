from random import randint

user_input = 'y'
count = 0

while user_input == 'y':
    rand_num = randint(1, 6)
    print("Random Number: %d" % rand_num)
    user_input = input("Would you like to try again? (y/n): ").lower()
    count += 1
print("You rolled the dice %d times" % count)
