# Class Starting with Python from www.alura.com.br
print("**************************")
print("Welcome to the Guess Game!")
print("**************************")

secret_number = 42
guess = input("Guess a number: ")

print("You entered: ", guess)

if (secret_number == int(guess)):
    print("You got the right number!")
else:
    print("You got wrong!")
