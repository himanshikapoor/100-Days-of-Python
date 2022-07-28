import hangman_words
import stages
import random
import os
from time import sleep

print(stages.logo)
chosen_word = random.choice(hangman_words.word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Make a list containing the guessed-words of user and a variable tracking lives of the user
display = []
lives = 6

for char in chosen_word:
  display.append("_")

while '_' in display and lives > 0:
    # Make a variable to input the guessed word of the user
    guess = input("Guess a letter: ").lower()
    os.system('cls')
    flag = 0
    # If the letter at that position matches guessed-word then reveal that letter in the display at that position
    for letter in chosen_word:
        if letter == guess:
            flag = 1
            for index in range(len(chosen_word)):
                if chosen_word[index] == letter:
                    display[index] = letter
    displayToStr = ' '.join(map(str, display))
    print(displayToStr)
    if flag != 0:
        print(stages.stages[lives])

    if flag == 0:
        print(f"You guessed {guess} and that's not in the word. You lose a life.")
        lives -= 1
        print(stages.stages[lives])
    
    sleep(0.2)

if lives == 0:
    print("You lose!")
else:
    print("You win!")