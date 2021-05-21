import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
guessed_states = []


def show_state_name(x, y, state):
    new_turtle = turtle.Turtle()
    new_turtle.hideturtle()
    new_turtle.penup()
    new_turtle.goto(x, y)
    new_turtle.write(state)


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 States Correct", prompt="What's another states's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in data["state"]:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
        
    for index, state in enumerate(data["state"]):
        if state == answer_state:
            show_state_name(data["x"][index], data["y"][index], state)
            guessed_states.append(state)



