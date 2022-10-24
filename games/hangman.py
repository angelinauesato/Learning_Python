# https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range

from email import message
import random

def play():
    open_message()
    
    secret_word = load_secret_word()
    
    correct_letters = initilize_letter(secret_word)

    print(correct_letters)

    win = False
    errors = 0
    lost = False
    
    while(not lost and not win):
        guess = ask_guess()

        if(guess in secret_word):
            right_guess(guess, secret_word, correct_letters)
        else:
            errors +=1
            print_hangman(errors)
            print(f"You got an error. You have {7 - errors}, chances. Try again.")
       
        lost = errors == 7
        print(correct_letters)
        win = "_" not in correct_letters

        if(not lost and win):
            message_win_game()
            break

    if(lost and not win):
        message_lost_game(secret_word)

def open_message():
    print("****************************")
    print("Welcome to the Hangman Game!")
    print("****************************")

def load_secret_word():
    file = open('words.txt', 'r')
    
    words = []

    for line in file:
        words.append(line.strip())
    file.close()
        
    number = random.randrange(0, len(words))
    
    secret_word = words[number]

    return secret_word

def initilize_letter(word):
    return ['_' for letter in word]

def ask_guess():
    guessed = input("Guess a letter:").strip()
    return guessed

def right_guess(guess, word, correct_letters):
    index = 0 
            
    for letter in word:
        if(guess.upper() == letter.upper()):
            correct_letters[index] = guess
        index +=1

def message_lost_game(word):
    print("Sorry, You lost!")
    print("The word was: {}".format(word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def message_win_game():
    print("Congratulations. You got it!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_hangman(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    play()
