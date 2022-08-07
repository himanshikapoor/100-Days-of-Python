MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0
shouldContinue = True
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def coin_operations(choice):
    """Returns change of the amount"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return round((0.25 * quarters + 0.1 * dimes + 0.05 * nickels + 0.01 * pennies) - MENU[choice]["cost"], 2)


def are_resources_sufficient(choice):
    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def reduce_resources(choice):
    if not are_resources_sufficient(choice):
        return False
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    return True


def is_transaction_successful(choice):
    change = coin_operations(choice)
    if change < 0:
        print("Not enough money provided. Money refunded.")
        return False
    print(f"Here is ${change} in change.")
    print(f"Here is your {choice} ☕. Enjoy!")
    return True


while shouldContinue is True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(f'Water: {resources["water"]} ml\nMilk: {resources["milk"]} ml\nCoffee: {resources["coffee"]} g\nMoney: ${money}')
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if not reduce_resources(choice):
            shouldContinue = False
        elif is_transaction_successful(choice):
            money += MENU[choice]["cost"]
    elif choice == "off":
        shouldContinue = False
