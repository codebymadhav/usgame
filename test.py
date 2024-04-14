import turtle
from turtle import Turtle,Screen
import pandas as pd

t=Turtle()
sc=Screen()
sc.title("is game")
image ='blank.gif'
sc.addshape(image)
t.shape(image)

data=pd.read_csv('50_states.csv')
all_states=data.state.to_list()
guessed_state=[]
while len(guessed_state) <50:
    answer_state=sc.textinput(title=f"{len(guessed_state)}/50 guess the name", prompt="What's another state name ?").title()


    if answer_state in all_states:
        guessed_state.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

sc.exitonclick()