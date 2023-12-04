from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()  # оєкт який получає гроші і рахує
coffee_maker = CoffeeMaker()  # обєкт який провіряє скільки інгрідієнтів в машині і створює ківу
menu = Menu()  # обєкт з списком всього асортимент
continues = True

while continues:
    name_coffee = input(f"What would you like? ({menu.get_items()}): ")
    if name_coffee == "off":
        continues = False
    elif name_coffee == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(name_coffee)  # получаю всепро заказану каву
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # провіряю чи достатньо інгрідієнтів і оплати
            coffee_maker.make_coffee(drink)  # створюю каву
