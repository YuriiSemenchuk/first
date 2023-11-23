from art import logo
from art import vs
from game_data import data
import random


def first(answers, b):
    if answers > 0:
        a = b[1]
    else:
        a = random.randint(0, len(data) - 1)
    print(f"Compare A: {data[a]['name']},"
          f" a {data[a]['description']},"
          f" from {data[a]['country']}")
    print(vs)
    return [data[a]['follower_count'], a]


def opposite():
    b = random.randint(1, len(data) - 1)
    print(f"Against B: {data[b]['name']},"
          f" a {data[b]['description']},"
          f" from {data[b]['country']}")
    return [data[b]['follower_count'], b]


def game():
    right_answers = 0
    b = []
    print(logo)
    while True:
        a = first(right_answers, b)
        b = opposite()
        answers = [a, b]
        if input("Who has more followers? Tipe 'A' or 'B': ").lower() == 'a':
            answer = 0
            not_answer = 1
        else:
            answer = 1
            not_answer = 0

        if answers[answer][0] < answers[not_answer][0]:
            print("You lose!")
            print(f"{data[a[1]]['name']} has {a[0]}m followers, {data[b[1]]['name']} has {b[0]}m followers")
            if input("Do you wont play again? 'y' or 'n': ") == 'n':
                return
            else:
                game()
                return
        else:
            right_answers += 1
            print(f"{data[a[1]]['name']} has {a[0]}m followers, {data[b[1]]['name']} has {b[0]}m followers")
            print(f"You right! Your score is {right_answers}")


game()
