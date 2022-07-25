import random

from matplotlib.style import use
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
choices = [rock, paper, scissors]
if user_choice >= 3 or user_choice < 0:
    print("Wrong Input. You lose")
else:
    print(choices[user_choice])
    comp_choice = random.randint(0,2)
    print("Computer chose:\n", choices[comp_choice])

    if user_choice == comp_choice:
        print("It's a draw.")
    elif user_choice == 0 and comp_choice == 2:
        print("You win!")
    elif user_choice > comp_choice:
        print("You win!")
    elif user_choice == 2 and comp_choice == 0:
        print("You lose")
    elif comp_choice > user_choice:
        print("You lose")