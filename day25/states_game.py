import pandas
import turtle
from turtle import Screen
from show_states import Show_states
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
show_states = Show_states()

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answers = 0
while answers != 50:
    answer = screen.textinput(title=f"{answers}/50 States Correct", prompt="What's another state's name?").title()
    if answer == "Exit":
        states_to_learn = {"states_to_learn": states}
        pandas.DataFrame(states_to_learn).to_csv("states_to_learn.csv")
        break
    if answer in states:
        answers += 1
        states.remove(answer)
        state_data = data[data.state == answer]
        print(state_data.x)
        show_states.show_state(answer, state_data.x, state_data.y)
