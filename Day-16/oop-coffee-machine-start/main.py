from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
machine = MoneyMachine()
menu = Menu()
shouldContinue = True

while shouldContinue:
    choice = input(f"What would you like? {menu.get_items()} ")
    if choice == "off":
        shouldContinue = False
    elif choice == "report":
        coffee_maker.report()
        machine.report()
    else:
        item = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(item) and machine.make_payment(item.cost):
                coffee_maker.make_coffee(item)
        else:
            shouldContinue = False

