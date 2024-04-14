import turtle
import pandas as pd

screen =turtle.Screen()
screen.title("u.s. state game")
image="blank.gif"
screen.addshape(image)
turtle.shape(image)

data=pd.read_csv("50_states.csv")
all_states=data['state'].to_list()




answer_state=screen.textinput(title="Guess the state",prompt=" ")
print(answer_state)

#if answer _state in data first row
if answer_state in all_states:
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data=data[data.state == answer_state]
    t.goto(state.x,state_data.y)
    t.write(state_data.state)

#else