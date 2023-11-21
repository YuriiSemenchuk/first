import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
         11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
your_cards = []
computer_cards = []


def give_card(who):  # получаю кому видати карту і видаю
    random_card = random.choice(cards)
    who.append(random_card)
    cards.remove(random_card)


def your_turn():  # видаю карти гравцю
    while True:
        give_card(your_cards)
        if sum(your_cards) > 21:  # і якщо рахунок більше 21 з заміняю карту 11 на 1 або видаю програш
            if your_cards.count(11) >= 1:
                your_cards.insert(your_cards.index(11), 1)
                your_cards.remove(11)
            else:
                print(f"your cards {your_cards}")
                print("You lose!")
                return True
        print(f"your cards {your_cards}")
        if input("Tipe 'y' to get card. Tipe 'n' to pass: ") == "n":
            return False


def computer_turn():  # видаю карти компютеру
    while sum(computer_cards) < 16:
        give_card(computer_cards)
        if sum(computer_cards) > 21:
            if computer_cards.count(11) >= 1:
                computer_cards.insert(computer_cards.index(11), 1)
                computer_cards.remove(11)
            else:
                print("You win!")
                return True
        print(f"computer cards {computer_cards}")
    return False


def check():  # провіряю хто виграв
    if sum(your_cards) == 21:
        print("You have Blackjack")
    if sum(your_cards) > sum(computer_cards):
        print("You win!")
    elif sum(computer_cards) > sum(your_cards):
        print("You lose!")
    else:
        print("Draw!")


def game():
    print(art.logo)
    give_card(your_cards)
    give_card(computer_cards)
    print(f"computer cards {computer_cards}")
    if your_turn():
        return
    if computer_turn():
        return
    print(f"Computer have {sum(computer_cards)}")
    print(f"You have {sum(your_cards)}")
    check()


game()
