import art
import os

print(art.logo)
print("Welcome to the Secret Auction Program.")

ans = "yes"
bidders = {}
while ans == "yes":
    name = input("What is your name? ")
    bid = int(input("What's your bid? Rs "))
    bidders[name] = bid
    ans = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if ans == "no":
        os.system('cls')
        max_bid = -1
        winner = ""
        for name in bidders:
            if max_bid < bidders[name]:
                max_bid = bidders[name]
                winner = name
        print(f"The winner is {winner} with a bid of Rs {max_bid}")
    else:
        os.system('cls')