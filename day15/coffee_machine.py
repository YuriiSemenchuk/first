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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def money(choice):
    # получаю оплату провіряю чи достаттньо
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    if choice["cost"] > total:
        print("Sorry that's not enough money. Money refunded")
        return False
    else:
        change = round(total - choice["cost"], 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += choice["cost"]
        return True


def enough_ingredients(choice):
    # провіряю чи достатньо інгрідієнтів
    for ingredient in choice["ingredients"]:
        if choice["ingredients"][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return True


def coffee():
    global profit
    name_coffee = input("What would you like? (espresso/latte/cappuccino): ")
    if name_coffee == "of":
        return True
    elif name_coffee == "report":
        print(resources["water"])
        print(resources["milk"])
        print(resources["coffee"])
        print(profit)
    else:
        choice = MENU[name_coffee]
        if enough_ingredients(choice):
            return False
        if money(choice):
            for resource in resources:
                # видаляю використані інгрідієнти
                resources[resource] -= choice["ingredients"][resource]
            print(f"Here is your {name_coffee} ☕️. Enjoy!")
        else:
            return False


coffees = 0
continues = True
while continues:
    if coffee():
        continues = False
    else:
        coffees += 1
print(coffees)
