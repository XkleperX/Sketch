from turtle import Turtle, Screen
from os import system

system("cls")

memo = Turtle()
screen = Screen()


def move_forward():
    memo.forward(10)


def move_backward():
    memo.backward(10)


def move_left():
    new_heading = memo.heading() + 10
    memo.setheading(new_heading)


def move_right():
    new_heading = memo.heading() - 10
    memo.setheading(new_heading)


def pen_up():
    memo.penup()


def pen_down():
    memo.pendown()


def clear_drawing():
    memo.clear()
    memo.penup()
    memo.home()
    memo.pendown()


memo.pensize(5)


up = input("enter the key you want to move forward: ")
down = input("enter the key you want to move backward: ")
left = input("enter the key you want to move left: ")
right = input("enter the key you want to move right: ")


screen.onkey(key=up, fun=move_forward)
screen.onkey(key=left, fun=move_left)
screen.onkey(key=right, fun=move_right)
screen.onkey(key=down, fun=move_backward)
screen.onkey(key="c", fun=clear_drawing)
screen.onkey(key="p", fun=pen_up)
screen.onkey(key="o", fun=pen_down)


screen.listen()
screen.exitonclick()
1
