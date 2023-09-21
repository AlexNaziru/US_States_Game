import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(height=491, width=725)
#setting my image path
image = "blank_states_img.gif"
screen.addshape(image)

#loading my image into turtle
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []#empty guessed states


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name? ").title()

    if answer_state == "Exit" or answer_state == "Quit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]#this is going to correspond each state to what the user writes
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))#like in JSON geo data used in my JS projects
        t.write(answer_state)

#saving data into an CSV



screen.bye()
#turtle.mainloop()

#an event listener for our mouse click coordinates on the screen
#def get_mouse_click_coor(x, y):
    #print(x, y)
#turtle.onscreenclick(get_mouse_click_coor)