import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def playgame():
    os.system('cls')
    print(art.logo)
    card_list = []
    compCard_list = []

    #initializing cards list of user and computer
    for _ in range(2):
        card_list.append(random.choice(cards))
        compCard_list.append(random.choice(cards))
    curr_score = sum(card_list)
    compCurr_score = sum(compCard_list)
    print(f"Your cards: {card_list}, current score: {sum(card_list)}")
    print(f"Computer's first card: {compCard_list[0]}")

    ch = input("Type 'y' to get another card, type 'n' to pass: ")
    while ch == 'y':
        card_list.append(random.choice(cards))
        curr_score += card_list[-1]
        if compCurr_score != 0 and compCurr_score < 17:
            compCard_list.append(random.choice(cards))
            compCurr_score += compCard_list[-1]

        # Condition of black jack (a hand with only two cards ace and 10) and change of value of ace if score is over 21
        if curr_score == 21 and len(card_list) == 2:
            curr_score = 0
        elif compCurr_score == 21 and len(compCard_list) == 2:
            compCurr_score = 0
        elif curr_score > 21 and 11 in card_list:
            card_list.remove(11)
            card_list.append(1)
            curr_score = sum(card_list)

        print(f"Your cards: {card_list}, current score: {curr_score}")
        if curr_score > 21 or compCurr_score == 0 or curr_score == 0:
            print("You went over. You lose!")
            ch = 'a'
        elif compCurr_score > 21:
            print("Computer went over. You win!")
            ch = 'a'
        else:
            ch = input("Type 'y' to get another card, type 'n' to pass: ")

    if ch == 'n':
        print(f"Your final hand: {card_list}, final score: {curr_score}")
        print(f"Computer's final hand: {compCard_list}, final score: {compCurr_score}")
        
        if compCurr_score == 0:
            print("You lose, computer has a black jack!")
        elif curr_score == 0:
            print("You win with a black jack!")
        elif compCurr_score > curr_score:
            print("You lose!")
        elif compCurr_score == curr_score:
            print("It's a draw.")
        else:
            print("You win!")

while input("Do you want to play the game of Black Jack? Type 'y' or 'n': ") == 'y':
    playgame()
