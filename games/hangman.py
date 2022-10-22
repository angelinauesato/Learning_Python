# https://docs.python.org/3.6/library/stdtypes.html#sequence-types-list-tuple-range

def play():
    print("****************************")
    print("Welcome to the Hangman Game!")
    print("****************************")
    
    secret_word = 'banana'
    correct_letters = ['_' for letter in secret_word]

    win = False
    errors = 0
    lost = False
    print(correct_letters)

    while(not lost and not win):
        guess = input("Guess a letter:").strip()

        if(guess in secret_word):
            index = 0 
            
            for letter in secret_word:
                if(guess.upper() == letter.upper()):
                    correct_letters[index] = guess
                index +=1
        else:
            errors +=1
            print(f"You got an error. You have {len(secret_word) - errors}, chances. Try again.")
        lost = errors == len(secret_word)
        print(correct_letters)
        win = "_" not in correct_letters
        if(not lost and win):
            print(f"Congratulations! You got it. {secret_word} was the secret word.")
            break
        
    print("End of the game.")
if(__name__ == "__main__"):
    play()