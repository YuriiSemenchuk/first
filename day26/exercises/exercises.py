def ex_1():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [number ** 2 for number in numbers]
    print(squared_numbers)


def ex_2():
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    result = [num for num in numbers if num % 2 == 0]
    print(result)


def ex_3():
    with open("file1") as file1:
        with open("file2") as file2:
            numbers1 = file1.readlines()
            numbers2 = file2.readlines()
    result = [int(num) for num in numbers1 if num in numbers2]
    print(result)


def ex_4():
    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    result = {word: len(word) for word in sentence.split()}
    print(result)


def ex_5():
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }
    weather_f = {day: temp * 9/5 + 32 for (day, temp) in weather_c.items()}
    print(weather_f)


ex_5()
