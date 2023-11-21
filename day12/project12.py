from art import logo
import random
NUMBER = random.randint(1, 100)


def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = 5
    if difficulty == "easy":
        turns = 10
    print(f"You have {turns} attempts remaining to guess the number.")
    while True:
        guess = int(input("Make a guess: "))
        if guess > NUMBER:  # провіряю чи гравець вгадав якщо ні пишу в якому напрямку рухатись
            print("Too high")
        elif guess < NUMBER:
            print("Too low")
        else:
            return True
        turns -= 1
        if turns > 0:  # провіряю чи в гравця залишились спроби
            print("Guess again.")
        elif turns == 0:
            return False


if game():
    print(f"You got it! The answer was {NUMBER}.")
else:
    print(f"You've run out of guesses, you lose! The answer was {NUMBER}.")
