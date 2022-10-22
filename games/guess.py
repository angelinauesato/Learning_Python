# Class Starting with Python from www.alura.com.br
# Python 3
print("**************************")
print("Welcome to the Guess Game!")
print("**************************")

secret_number = 42
total_try = 3
got_right = False
for tries in range(1, total_try+1): # range(start, stop, [step])
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
        print("You got the right number!")
        break
    else:
        if bigger_guessed:
            print("You got wrong! The secret number is less than guessed number!")
        else:
            print("You got wrong! The secret number is bigger than guessed number!")
print("End of the game.")