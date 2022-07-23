print("Welcome to the tip calculator.")
bill_amt = float(input("What was the total bill? Rs "))
per = float(input("What percentage tip would you like to give? 10, 12 or 15? ")) / 100
people = int(input("How many people to split the bill? "))
amt_per_person = "{:.2f}".format((bill_amt * (1 + per)) / people)
print(f"Each person should pay: Rs {amt_per_person}")