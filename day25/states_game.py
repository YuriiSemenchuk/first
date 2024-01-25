import pandas
import turtle

data = pandas.read_csv("50_states.csv")
not_guessed_states = data.state.to_list()

screen = turtle.Screen()  # створюю екран з картою штатів америки
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.color("black")

answers = 0
while answers != 50:  # получаю відповіді провіряю чи вони правильні показую вгадані штати
    answer = screen.textinput(title=f"{answers}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        pandas.DataFrame(not_guessed_states).to_csv("states_to_learn.csv")
        break
    if answer in not_guessed_states:
        answers += 1
        not_guessed_states.remove(answer)
        state_data = data[data.state == answer]
        writer.goto(int(state_data.x), int(state_data.y))
        writer.write(arg=answer)
