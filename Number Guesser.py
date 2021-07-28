import random

max_num = input("Type a maximal number to guess: ")
try:
    number = random.randint(0, int(max_num))
except:
    print("Please enter a valid integer!")
    quit()
total_guess = 1

while True:
    guess = input("Guess a number between 0 and " + max_num + ": ")
    if guess.isdigit():
        if int(guess) == number:
            break
        elif int(guess) != number:
            total_guess += 1
            if int(guess) > number:
                print("Too big! Guess again!")
            if int(guess) < number:
                print("Too small! Guess again!")
    else:
        print("Please enter a valid integer!")
        quit()

print("You guess it right after", total_guess, "tries!")