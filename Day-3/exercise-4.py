# Program to build an automatic pizza order program
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total_bill = 0
if size == 'S':
    if add_pepperoni == 'Y':
        total_bill += 17
    else:
        total_bill += 15
elif size == 'M':
    if add_pepperoni == 'Y':
        total_bill += 23
    else:
        total_bill += 20
else:
    if add_pepperoni == 'Y':
        total_bill += 28
    else:
        total_bill += 25

if extra_cheese == 'Y':
    total_bill += 1

print(f"Your final bill is: ${total_bill}")