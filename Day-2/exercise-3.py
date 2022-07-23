# Program that tells us how many days, weeks, months we have left if we live until 90 years old.
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below  this line 👇
days_left = 365 * (90 - int(age)) 
weeks_left = 52 * (90 - int(age))
months_left = 12 * (90 - int(age))

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
