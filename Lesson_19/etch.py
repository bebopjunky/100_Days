from turtle import Turtle, Screen


bob = Turtle()
screen = Screen()


def move_fwd():
    bob.forward(10)

def move_bck():
    bob.backward(10)

def turn_lft():
    bob.left(5)

def turn_rgt():
    bob.right(5)

screen.listen()
screen.onkey(key="w",fun=move_fwd)
screen.onkey(key="s",fun=move_bck)
screen.onkey(key="a",fun=turn_lft)
screen.onkey(key="d",fun=turn_rgt)

screen.exitonclick()

