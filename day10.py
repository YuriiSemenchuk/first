def day10_1():
    def is_leap(year_for_leap):  # визначє чи рік високосний
        if year_for_leap % 4 == 0:
            if year_for_leap % 100 == 0:
                if year_for_leap % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def days_in_month(year_for_day, month_for_day):  # визначає скільки днів в місяці
        if is_leap(year_for_day) and month_for_day == 2:  # якщо рік високосний і місяц 2 то повертаю 29
            return 29
        else:  # інакше повертаю кількість днів в місяці під номером з масиву
            return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month_for_day - 1]

    year = int(input("Enter a year: "))
    month = int(input("Enter a month: "))
    print(days_in_month(year, month))


def day10():
    logo = """
         _____________________
        |  _________________  |
        | | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
        | |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
        |  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
        | | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
        | |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
        | | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
        | |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
        | | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
        | |___|___|___| |___| | | |              | || |              | || |              | || |              | |
        | | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
        | |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
        |_____________________|
        """
    print(logo)

    def plus(n1, n2):
        return n1 + n2

    def minus(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        return n1 / n2
# функції які виконують дії

    operations = {
        "+": plus,
        "-": minus,
        "*": multiply,
        "/": divide
    }  # словник за допомогою якого буду виклткати ці функції

    def calculator():
        num1 = float(input("What's the first number? "))
        finish = "y"
        while finish == "y":
            for symbol in operations:  # виводжу символи
                print(symbol)
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What's the second number? "))
            answer = operations[operation_symbol](num1, num2)  # викликаю функцію дії з словника і записую відповідь
            print(f"{num1} {operation_symbol} {num2} = {answer}")
            if input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ") == "y":
                # провіряю чи продовжувати з цим числом чи ввести нове
                num1 = answer
            else:
                finish = "n"
                calculator()
    calculator()


day10()
