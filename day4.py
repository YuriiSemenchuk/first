import random


def day4_1():
    randon_side = random.randint(0, 1)  # беру випадкове число
    if randon_side == 1:  # провіряю що вивести
        print("Heads")
    else:
        print("Tails")


def day4_2():
    names_string = input("give me everybody's names, seperated by a comma ")  # получаю список людей в масив
    names = names_string.split(",")  # перетворюю строку в масив розбившиїї на змінні
    print(random.choice(
        names) + " is going to buy the meal today!")  # вибиваю випадкове імя з масиву і пишу хто йде купляти


def day4_3():
    row1 = ["🛟", "🛟", "🛟"]  # створюю масив першої лінії карти
    row2 = ["🛟", "🛟", "🛟"]  # створюю масив другої лінії карти
    row3 = ["🛟", "🛟", "🛟"]  # створюю масив третьої лінії карти
    a_map = [row1, row2, row3]  # створюю масив з масивів ліній карти
    print(f"  {row1}\n  {row2}\n  {row3}")  # вивожу карту
    position = input("Where do you wont to put the treasure? ")  # получаю відповідь користувача де клад
    vertical = int(position[1]) - 1  # визначаю в якому масиві клад
    horizontal = int(position[0]) - 1  # визначаю на якій позиції клад
    a_map[vertical][horizontal] = "x"  # міняю змінну на х масиві в масиві з масивів
    print(f"  {row1}\n  {row2}\n  {row3}")  # вивожу змінену карту


def day4():
    user_choose = int(
        input("What do you choose? tipe 0 for Rok 1 fir Paper 2 for Scissors "))  # визначаю відповідь користувача
    if user_choose != 0 or user_choose != 1 or user_choose != 2:  # провіряю чи відповіди підходить
        print("You typed invalid number. You lose")
    else:
        chooses = ["Rok ✊", "Paper ✋", "Scissors ✌️"]  # створюю масив з варіантами відповіді
        print("you choose:")
        print(chooses[user_choose])  # вивожу відповідь користувача
        print("computer choose:")
        computer_choose = random.randint(0, 2)  # створюю випадкуву відповідь компютера
        print(chooses[computer_choose])  # вивожу відповідь компютера
        if user_choose == 0 and computer_choose == 2:  # провіряю хто виграв
            print("You win")
        elif user_choose == 1 and computer_choose == 0:
            print("You win")
        elif user_choose == 2 and computer_choose == 1:
            print("You win")
        elif computer_choose == user_choose:
            print("Draw")
        else:
            print("You lose")


day4()
