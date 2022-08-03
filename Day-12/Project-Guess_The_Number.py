import art
import random

print(art.logo, "Welcome to the Guess the Number game!")
level = input("Choose a difficulty. Type easy or hard. ")

def lowGuess(attempts):
    """Returns messages for making a guess lesser than the number"""
    attempts -= 1
    print("Too low.\nGuess Again!")
    print(f"You have {attempts} attempts remaining.")
    return attempts

def highGuess(attempts):
    """Returns messages for making a guess greater than the number"""
    print("Too high.\nGuess Again!")
    print(f"You have {attempts} attempts remaining.")
    return attempts

def result(attempts, guess, chosen_no):
    """Returns the result of the game"""
    if attempts == 0 and guess != chosen_no:
        print("You have run out of guesses. You lose!")
    else:
        print(f"You got it! The answer was {chosen_no}")

# Choosing a number from 1 to 100
chosen_no = random.randint(1, 100)

if level == "easy":
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    while guess != chosen_no and attempts != 0:
        if guess < chosen_no:
            attempts = lowGuess(attempts)
            guess = int(input("Make a guess: "))
        else:
            attempts = highGuess(attempts)
            guess = int(input("Make a guess: "))
else:
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))

    while guess != chosen_no and attempts != 0:
        if guess < chosen_no:
            attempts = lowGuess(attempts)
            guess = int(input("Make a guess: "))
        else:
            attempts = highGuess(attempts)
            guess = int(input("Make a guess: "))
    
result(attempts, guess, chosen_no)