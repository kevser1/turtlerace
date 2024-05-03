import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet",prompt="Witch turtle winn the race? Enter a color:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)
if user_bet: #user bet var mı yok mu kontrolü
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is a winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is a winner!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)





"""
tim = Turtle(shape="turtle")
tim.color("blue")
tim.penup()
tim.goto(x=-230, y=-100)

timmy = Turtle(shape="turtle")
timmy.color("red")
timmy.penup()
timmy.goto(x=-230, y=-70)

benny = Turtle(shape="turtle")
benny.color("green")
benny.penup()
benny.goto(x=-230, y=-40)

cimmy = Turtle(shape="turtle")
cimmy.color("yellow")
cimmy.penup()
cimmy.goto(x=-230, y=-10)

gorge = Turtle(shape="turtle")
gorge.color("orange")
gorge.penup()
gorge.goto(x=-230, y=20)

adam = Turtle(shape="turtle")
adam.color("purple")
adam.penup()
adam.goto(x=-230, y=50)
"""




screen.exitonclick()