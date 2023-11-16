def day3_1():
    number = int(input("witch number do you want to check? "))  # получаю число
    if number % 2 == 0:  # провіряю парне воно чи ні
        print("this is a even number")
    else:
        print("this is an odd number")


def day3_2():
    weight = float(input("скільки ти важиш? "))  # получаю вагу
    height = float(input("який в тебе ріст? "))  # получаю ріст
    bmi = round(int(weight / height ** 2), 1)  # вираховую індекс маси тіла
    if bmi < 18.5:  # провіряю який у нього індекс маси тіла і видаю
        print(f"your BMI is {bmi}, you are underweight")
    elif bmi < 25:
        print(f"your BMI is {bmi}, you are normal weight")
    elif bmi < 30:
        print(f"your BMI is {bmi}, you are overweight")
    elif bmi < 35:
        print(f"your BMI is {bmi}, you are obese")
    else:
        print(f"your BMI is {bmi}, you are clinically obese")


def day3_3():
    year = int(input("which year do you want to check? "))  # получаю рік
    if year % 4 == 0:  # провіряю чи він високосний і видаю результат
        if year % 100 == 0 and year % 400 == 0:
            print("leap year")
        elif year % 100 != 0:
            print("leap year")
        else:
            print("not leap year")

    else:
        print("not leap year")


def day3_4():
    print("Welcome to Python Pizza Deliveries!")
    size = input("What size  pizza do you want? S, M, or L ")  # получаю розмір піци
    add_pepperoni = input("Do you want pepperoni? Y or N ")  # взнаю чи добавляти пепероні
    extra_cheese = input("Do you want extra cheese? Y or N ")  # взнаю чи добавляти додатковий сир
    bill = 0
    if size == "S":  # провіряю розмір піци і добавляю ціну
        bill += 15
    elif size == "M":
        bill += 20
    else:
        bill += 25
    if add_pepperoni == "Y":  # провіряю добавляння пепероні і додаю до суми якшо є
        if size == "S":
            bill += 2
        else:
            bill += 3
    if extra_cheese == "Y":  # провіряю добавляння додаткового сиру і додаю до суми якшо є
        bill += 1
    print(f"Your final bill is {bill}")


def day3_5():
    print("Welcome to the Love Calculator!")
    name1 = input("What is your name? \n").lower()  # взнаю перше ім'я і міняю всі букви на малі
    name2 = input("What is their name?\n").lower()  # взнаю перше ім'я і міняю всі букви на малі
    combined_names = name2 + name1  # додаю їх
    score = (combined_names.count("t") + combined_names.count("r") + combined_names.count("u") + combined_names.count(
        "e")) * 10
    score += combined_names.count("l") + combined_names.count("o") + combined_names.count("v") + combined_names.count(
        "e")  # рахую очки
    if score < 10 or score > 90:  # оприділяю що написати
        print(f"Your score is {score}, you go together like coke and mentos")
    elif 40 <= score <= 50:
        print(f"Your score is {score}, you are alright together")
    else:
        print(f"Your score is {score}")


def day3():
    print("game")
    print("Welcome to Treasure Island")
    print("Your mission is to find the treasure")
    answer1 = input(
        "You are at a cross road. Where do you want to go? Type 'left' or 'right' ").lower()  # визначаю відповідь користувача
    if answer1 == "left":  # оприділяю чи відповідь правильна і реагую
        answer2 = input(
            "You come to a lace. There is an island in the middle of lace. Tipe 'wait' to wait the boat. Type 'swim' to swim across ").lower()  # визначаю відповідь користувача
        if answer2 == "wait":  # оприділяю чи відповідь правильна і реагую
            answer3 = input(
                "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, one blue. Wich color do you choose? ").lower()  # визначаю відповідь користувача
            if answer3 == "yellow":  # оприділяю чи відповідь правильна і реагую
                print("You found a treasure. You Win!")
            elif answer3 == "blue":
                print("You enter a room of beasts. Game over")
            elif answer3 == "red":
                print("It is a room full of fire. Game over")
            else:
                print("Нou went aut. Game over")
        else:
            print("you got attacked by angry trout. Game over ")
    else:
        print("you fell into a hole. Game over")


day3()
