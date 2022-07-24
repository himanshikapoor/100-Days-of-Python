# Program that tests the compatibility between two people 
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()
combined_name = name1 + name2
true_count = combined_name.count("t") + combined_name.count("r") + combined_name.count("u") + combined_name.count("e")
love_count = combined_name.count("l") + combined_name.count("o") + combined_name.count("v") + combined_name.count("e")
total_count = true_count * 10 + love_count

if total_count < 10 or total_count > 90:
    print(f"Your score is {total_count}, you go together like coke and mentos.")
elif total_count > 40 and total_count < 50:
  print(f"Your score is {total_count}, you are alright together.")
else:
  print(f"Your score is {total_count}")