from turtle import Turtle,Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Bet",prompt="Who will win?: ")
colours = ["red","orange","yellow","green","blue","purple"]
y_pos = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.goto(x=-200,y=y_pos[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() >230:
            winning_colour = turtle.pencolor()
            if winning_colour == user_bet:
                print("Winner Winner Chicken Dinner!")
                pass
            else:
                print("Loser")
            is_race_on = False

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()