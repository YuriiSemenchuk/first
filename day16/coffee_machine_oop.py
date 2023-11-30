from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
continues = True

while continues:
    name_coffee = input(f"What would you like? ({menu.get_items()}): ")
    if name_coffee == "off":
        continues = False
    elif name_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(name_coffee)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
