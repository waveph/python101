from turtle import Turtle, Screen


tom = Turtle()



screen = Screen()
screen.listen()

def move_forward():
    tom.forward(10)

def move_backward():
    tom.backward(10)

def clock_wise():
    tom.right(10)

def counter_clock_wise():
    tom.left(10)

def clear_screen():
    tom.penup()
    tom.goto(0, 0)
    tom.clear()
    tom.setheading(0)



screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key="c", fun=clear_screen)














screen.exitonclick()