import turtle
import pandas
from turtle import Screen, Turtle

# Setup screen
screen = Screen()
state_write = Turtle()
state_write.hideturtle()
state_write.penup()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Load data
data = pandas.read_csv("50_states.csv")
list_of_state = data["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name? (or type 'exit' to quit)"
    )

    if answer_state is None or answer_state.lower() == "exit":
        break

    answer_state = answer_state.title()

    if answer_state in list_of_state and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)

        state_write.goto(x, y)
        state_write.write(answer_state, align="center", font=("Arial", 8, "normal"))

screen.mainloop()
