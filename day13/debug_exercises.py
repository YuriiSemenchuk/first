def ex_1():
    number = int(input("Which number do you want to check?"))
    if number % 2 == 0:  # bug was hear
        print("This is an even number.")
    else:
        print("This is an odd number.")


def ex_2():
    year = int(input("Which year do you want to check?"))  # bug was hear
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def ex_3():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


ex_3()
