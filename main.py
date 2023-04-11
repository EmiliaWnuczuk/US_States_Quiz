import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()
screen.tracer(0)

score = 0
answer = screen.textinput(title="Guess the State", prompt="What's the first state name?")
answer_state = answer.title()

states = pandas.read_csv("50_states.csv")
all_states = states.state.to_list()
guessed_states = []

game_is_on = True

while game_is_on:

    if answer_state == "Exit":
        states_to_learn = [state for state in all_states if state not in guessed_states]
        # states_to_learn = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in all_states:
        score += 1
        guessed_states.append(answer_state)
        guess_state = states[states["state"] == answer_state]
        xcor = int(guess_state.x)
        ycor = int(guess_state.y)
        turtle.goto(xcor, ycor)
        turtle.write(answer_state)
        turtle.goto(0, 0)
        answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")
        answer_state = answer.title()
    else:
        answer = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state name?")
        answer_state = answer.title()

    screen.update()

# turtle.mainloop()
# screen.exitonclick()