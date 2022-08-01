import art
import os

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide,
}

def calculator():
    print(art.logo)
    n1 = float(input("What's the first number? "))
    n2 = float(input("What's the next number? "))

    for key in operations:
        print(key)
    operation = input("Pick an operation from the line above: ")
    ans = operations[operation](n1, n2)
    print(f"{n1} {operation} {n2} = {ans}")

    choice = input(f"Type 'yes' to continue calculating with {ans} or 'no' to exit: ")
    while choice == "yes":
        newAns = ans
        op = input(f"Pick an operation to continue calculation with {ans}: ")
        n2 = float(input("What's the next number? "))
        newAns = operations[op](ans, n2)
        print(f"{n2} {op} {ans} = {newAns}")

        choice = input(f"Type 'yes' to continue calculating with {newAns} or 'no' to start another calculation: ")
        if choice == "no":
            os.system('cls')
            calculator()
calculator()