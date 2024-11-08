from turtle import Turtle,Screen

screen=Screen()
paddle=Turtle()

screen.title("Pong Game")
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle.shape("square")
paddle.color("red")
paddle.turtlesize(stretch_wid=5,stretch_len=1)
paddle.penup()
paddle.setposition(x=350,y=0)

def go_up():
    new_y = paddle.ycor()+20
    paddle.goto(paddle.xcor(),new_y)

def go_down():
    new_y = paddle.ycor()-20
    paddle.goto(paddle.xcor(),new_y)

screen.listen()
screen.onkey(go_up, "w")
screen.onkey(go_down, "s")

game_is_on=True
while game_is_on:
    screen.update() 

screen.exitonclick()