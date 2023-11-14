def day9_1():
    student_scores = {
        "Harry": 81,
        "Ron": 78,
        "Hermione": 99,
        "Draco": 74,
        "Neville": 62,
    }  # словник з балами студентів
    student_grades = {}
    for student in student_scores:  # провіряю які студенти пройшли і записую їх результати в словник
        if student_scores[student] > 90:
            student_grades[student] = "Outstanding"
        elif student_scores[student] > 80:
            student_grades[student] = "Exceeds Expectations"
        elif student_scores[student] > 70:
            student_grades[student] = "Acceptable"
        else:
            student_grades[student] = "Fail"

    print(student_grades)


def day9_2():
    travel_log = [
        {
            "country": "France",
            "visits": 12,
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "country": "Germany",
            "visits": 5,
            "cities": ["Berlin", "Hamburg", "Stuttgart"]
        },
    ]  # масив з словарями країн і міст які відвідав

    def add_new_country(country, visits, cities):  # додає до масиву словар з країною і містами які відвідав
        travel_log.append({"country": country,
                           "visits": visits,
                           "cities": cities,
                           })

    add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
    print(travel_log)


def day9():
    logo = '''
                             ___________
                             \         /
                              )_______(
                              |"""""""|_.-._,.---------.,_.-._
                              |       | | |               | | ''-.
                              |       |_| |_             _| |_..-'
                              |_______| '-' `'---------'` '-'
                              )"""""""(
                             /_________\\
                           .-------------.
                          /_______________\\
    '''
    print(logo)
    bidders = "yes"
    auction_users = []
    while bidders == 'yes':  # додаю імена і ставки учасникув аукціону в масив з словників
        name = input("What is your name?: ")
        bid = int(input("What's your bid?: "))
        bidders = input("Are there any bidders? Tipe 'yes' or 'no'").lower()
        auction_users.append({"name": name,
                              "bid": bid,
                              })

    max_bid = 0
    winner = "no one participated"
    for i in range(len(auction_users)):  # провіряю в кого найвища ставка
        if auction_users[i]["bid"] > max_bid:
            max_bid = auction_users[i]["bid"]
            winner = auction_users[i]["name"]
    print(f"The winner is {winner} with bid of ${max_bid}.")  # вивожу імя і ставку вигравшого


day9()
