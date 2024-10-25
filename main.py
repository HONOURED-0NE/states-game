import turtle

screen = turtle.Screen()
screen.title("U.S State Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
import pandas
# if u wanna get coordinate of wherever thee ouse clicks but since we alrdy got the values
#def get_mouse_click_coor(x, y):
#    print(x, y)
#
#turtle.onscreenclick(get_mouse_click_coor)
#turtle.mainloop()

data = pandas.read_csv('50_states.csv')
all_state = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    state_answer = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="Guess a state name").title()
    if state_answer == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states ]
        #for state in all_state:
            #if state not in guessed_states:
                #missing_states.append(state)
    #this function can be cut down usinglist comprehension
    # new_list = [new_item for item in list if test] (this is the format of lc one you fully grasp the concept youll be able to reduce your code by a large margin)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('States to learn.csv')
        break
    if state_answer in all_state:
        guessed_states.append(state_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_answer)
