from pickletools import read_uint1
import art
import game_data
import random
import os

score = 0
def chooseFromCandidates(a, b):
    """Returns the choice of the user"""
    print("Compare A: " + a["name"] + ", a " + a["description"] + ", from " + a["country"] + ".")
    print(art.vs)
    print("Against B: " + b["name"] + ", a " + b["description"] + ", from " + b["country"] + ".")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper()
    return choice

def checkCandidates(a, b):
    while a == b:
        b = random.choice(game_data.data)
    return b

def newIteration(a, b, score):
    """Returns choice of new iteration"""
    print(f"You're right! Current score: {score}")
    b = random.choice(game_data.data)
    b = checkCandidates(a, b)
    choice = chooseFromCandidates(a, b)
    return choice

a = random.choice(game_data.data)
b = random.choice(game_data.data)
b = checkCandidates(a, b)
choice = chooseFromCandidates(a, b)
continueGame = True

while continueGame is True:
    print(art.logo)
    os.system('cls')

    if choice == 'A' and a["follower_count"] >= b["follower_count"]:
        score += 1
        choice = newIteration(a, b, score)    
    elif choice == 'B' and a["follower_count"] <= b["follower_count"]:
        score += 1
        choice = newIteration(a, b, score)     
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        continueGame = False
