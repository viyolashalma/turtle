from turtle import Turtle,Screen
tim=Turtle()
my_screen=Screen()
tim.shape("turtle")
tim.speed(0)
for i in range(180):
    tim.circle(100)
    tim.left(2)
my_screen.exitonclick()