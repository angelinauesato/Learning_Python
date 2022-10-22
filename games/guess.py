# Class Starting with Python from www.alura.com.br
# Python 3
print("**************************")
print("Welcome to the Guess Game!")
print("**************************")

secret_number = 42
total_try = 3
tries = 0
got_right = False
while tries < total_try and (not got_right):
    tries += 1
    # String Interpolation
    # print("Round: {} of {}".format(tries, total_try))
    print(f"Round: {tries} of {total_try}")
    guess_str = input("Guess a number: ")

    print("You entered: ", guess_str)
    guess = int(guess_str)

    got_right = secret_number == guess
    bigger_guessed = secret_number < guess

    if got_right:
        print("You got the right number!")
    else:
        if bigger_guessed:
            print("You got wrong! The secret number is less than guessed number!")
        else:
            print("You got wrong! The secret number is bigger than guessed number!")
print("End of the game.")