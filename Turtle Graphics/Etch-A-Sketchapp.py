from turtle import Turtle,Screen

tim=Turtle()
screen=Screen()

def move_forward():
    '''This allow the turtle to move forward by 10 spaces'''
    tim.forward(10)

def move_backward():
    '''This allow the turtle to move backwar by 10 spaces'''
    tim.backward(10)

def clear_screen():
    '''This allow to remove the drawing but keep the turtle at it's current position'''
    tim.clear()

def reset_turtle():
    '''This allow to remove the drawinng and place the turtle at the center of the screen'''
    tim.reset()

def turn_left():
    '''This allow the turtle to turn to left by 10 deg'''
    new_heading=tim.heading()+10
    tim.setheading(new_heading) 
    #we can also use the left() function 

def turn_right():
    '''This allow the turtle to turn to right by 10 deg'''
    new_heading=tim.heading()-10
    tim.setheading(new_heading)
    #we can also use the right() function

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backward)
screen.onkey(key="a",fun=turn_left)
screen.onkey(key="d",fun=turn_right)
screen.onkey(key="c",fun=clear_screen)
screen.onkey(key="r",fun=reset_turtle)
screen.exitonclick()