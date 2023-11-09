def day5_1():
    student_heights = input("Input a list of student heights ").split()  # получаю висоти студентів і записую їх в масив
    for n in range(0, len(student_heights)):  # перетворюю всі значення висот в тип int
        student_heights[n] = int(student_heights[n])
    sum_heights = 0
    len_student_heights = 0
    for sum in student_heights:  # вираховую суму всіх висот і кількість студентів
        sum_heights += sum
        len_student_heights += 1
    print(int(sum_heights / len_student_heights))  # вираховую середню висоту і вивожу її


def day5_2():
    student_scores = input("Input a list of student scores ").split()  # получаю очки студентів і записую їх в масив
    for n in range(len(student_scores)):  # перетворюю всі очки в тип int
        student_scores[n] = int(student_scores[n])
    print(student_scores)  # вивожу масив очків студентів
    max_score = 0
    for score in student_scores:  # записуюю значення масива в змінну довжину масива раз
        if score > max_score:  # визначаю максимальний рахунок
            max_score = score
    print(f"max student score is {max_score}")  # вивожу максимальний рахунок


def day5_3():
    sum = 0
    for number in range(2, 101, 2):  # знаходжу суму чисел від 1 до 100 з кроком в два
        sum += number
    print(sum)  # вивожу суму


def day5_4():
    for number in range(1, 101):  # получаю число під номером повторення
        if number % 3 == 0 and number % 5 == 0:  # провіряю що маю вивести і виводжу
            print("FizzBuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


def day5():
    import random
    letters_number = int(input("Haw many letters wold you like?\n"))  # получаю бажану кількусть літер в паролі
    symbols_number = int(input("Haw many symbols wold you like?\n"))  # получаю бажану кількість символів в паролі
    numbers_number = int(input("Haw many numbers wold you like?\n"))  # получаю бажану кількість чисел в паролі
    letters = ['A', 'E', 'I', 'O', 'U', 'Y', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
               'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z', 'a', 'e', 'i', 'o', 'u', 'y', 'b', 'c',
               'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', ' n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x',
               'z']  # створюю масив з усіма англійськими літерами
    symbols = ["!", "#", "$", "%", "&", "*", "+", "(", ")"]  # створюю масив з символами
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # створюю масив з числами
    password_in_order = [letters, symbols, numbers]  # створюю масив з масивів усіх літер символів і чисел
    password = ""
    numbers_n = 0
    letters_n = 0
    symbols_n = 0
    while len(password) != numbers_number + letters_number + symbols_number:  # повторюю поки кількість симв
        random_number = random.randint(0, 2)  # визначаю літеру символ чи число зараз добавити
        if random_number == 0 and letters_n < letters_number:  # провіряю чи повинен поставити літеру і чи добавлено достатньо літер
            password += password_in_order[0][random.randint(0, len(letters) - 1)]  # якщо так то доставляю літеру
            letters_n += 1  # записуюю що доставив літеру
        elif random_number == 1 and numbers_n < numbers_number:  # провіряю чи повинен поставити число і чи добавлено достатньо чисел
            password += password_in_order[1][random.randint(0, len(numbers) - 1)]  # якщо так то доставляю число
            numbers_n += 1  # записуюю що доставив число
        elif random_number == 2 and symbols_n < symbols_number:  # провіряю чи повинен поставити символ і чи добавлено достатньо символів
            password += password_in_order[2][random.randint(0, len(symbols) - 1)]  # якщо так то доставляю символ
            symbols_n += 1  # записуюю що доставив символ
    print(password)


day5()
