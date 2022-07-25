# Program that will select a random name from a list of names
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
rand_index = random.randint(0, len(names) - 1)
print(f"{names[rand_index]} is going to buy the meal today!")

# Another Solution
# person = random.choice(names)
# print(person + "is going to buy the meal today!")