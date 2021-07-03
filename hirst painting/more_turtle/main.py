from turtle import Turtle, Screen

tim = Turtle()
screen = Screen() 

def move_forward():
    tim.forward(100)

def move_backwards():
    tim.backward(100)

def clock_wise():
    tim.right(10)

def counter_clock_wise():
    tim.left(10)   

def clear_screen():
    tim.reset()

def circle():
    tim.circle(40,40)


screen.listen()
screen.onkey(key='w',  fun=move_forward)

screen.onkey(key='s',  fun=move_backwards)

screen.onkey(key='d',  fun=clock_wise)

screen.onkey(key='a',  fun=counter_clock_wise)

screen.onkey(key='c',  fun=clear_screen)

screen.onkey(key='o',  fun=circle)










screen.exitonclick()
