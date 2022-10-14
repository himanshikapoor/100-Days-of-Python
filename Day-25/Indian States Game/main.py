import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
image = "Indian States Game/Indian_Map.gif"
screen.addshape(image)
turtle.shape(image)

score = 0
guessed_states = []

# Creating a turtle to write the names on map
my_turtle = turtle.Turtle()
my_turtle.hideturtle()
my_turtle.penup()

data = pandas.read_csv("Indian States Game/States.csv")

while score < 37:
    answer = screen.textinput(title=f"{score}/37 States Correct", 
                              prompt="What's another state's name?").title()

    # Breaking out of loop using special keyword
    if answer == "Exit":
        break
    
    # Checking if Data Exists in the csv file
    if answer in data.state.unique():
        my_turtle.goto(x=int(data[data.state == answer].x), y=int(data[data.state == answer].y))
        my_turtle.write(f"{answer}", align="center", font=("Courier", 8, "normal"))
        guessed_states.append(answer)
        score += 1

# Generating a csv file of states not known
state_list = data.state.to_list()
not_guessed_states_list = [state for state in state_list if state not in guessed_states]

df = pandas.DataFrame(not_guessed_states_list)
df.to_csv("Indian States Game/States_Not_Guessed.csv")

# # Code to get co-ordinates of states 
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()