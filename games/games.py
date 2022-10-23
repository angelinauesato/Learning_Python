import guess
import hangman

def choose_game():
    print("****************************")
    print("*****Choose your Game!******")
    print("****************************")
    print(" 1 - Hangman. \n 2 - Guess Number.\n")

    game = int(input("Choose the number of the game: "))

    if game == 1:
        print("Starting Hangman...")
        hangman.play()
    elif game == 2:
        print("Starting Guess Number...")
        guess.play()
if(__name__ == "__main__"):
    choose_game()