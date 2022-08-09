from turtle import Turtle, Screen

# creating an object of type Turtle
tim = Turtle()
print(tim)
tim.shape("turtle")
tim.color("cyan")
tim.forward(100)

# creating another object of type Screen
my_screen = Screen()
# using attribute - canvheight of the object
print(my_screen.canvheight)
# using method or function associated with object
my_screen.exitonclick()
