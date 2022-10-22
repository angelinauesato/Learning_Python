# Class Starting with Python from www.alura.com.br
# Python 3
# Python Libraries: https://docs.python.org/3/library/

import random


def play():
    print("**************************")
    print("Welcome to the Guess Game!")
    print("**************************")

    secret_number = random.randrange(1, 101)
    total_try = 0
    points = 1000

    print("Level of difficulty: ")
    print(" 1 - Easy. \n 2 - Intermediate. \n 3 - Hard.")
    level = int(input("Enter the number of the level: "))

    if level == 1:
        total_try = 20
    elif level == 2:
        total_try = 10
    else:
        total_try = 5

    for tries in range(1, total_try+1):  # range(start, stop, [step])
        # String Interpolation
        # print("Round: {} of {}".format(tries, total_try))
        print(f"Round: {tries} of {total_try}")
        guess_str = input("Guess a number between 1 and 100: ")
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("Please, You have to enter a number between 1 and 100!")
            continue

        print("You entered: ", guess_str)

        got_right = secret_number == guess
        bigger_guessed = secret_number < guess

        if got_right:
            print(f"You got the right number and scored {points} points!")
            break
        else:
            if bigger_guessed:
                print("You got wrong! The secret number is less than guessed number!")
            else:
                print("You got wrong! The secret number is bigger than guessed number!")
            lost_points = abs(secret_number - guess)
            points = points - lost_points
    print("End of the game.")
if(__name__ == "__main__"):
    play()