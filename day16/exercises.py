def tables():
    from prettytable import PrettyTable
    table = PrettyTable()
    table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"

    print(table)


def turtle():
    from turtle import Turtle, Screen

    timmy = Turtle()
    print(timmy)
    timmy.shape("turtle")
    timmy.color("coral")

    my_screen = Screen()
    print(my_screen.canvheight)
    timmy.forward(100)

    my_screen.exitonclick()


tables()
