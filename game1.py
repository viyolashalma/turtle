import random
from turtle import Turtle, Screen
turtle_list=[]
colors=['red','green','blue','yellow','pink','orange','black','violet']
my_screen=Screen()
my_screen.bgcolor("black")
ycor=[0,80,160,-80,-160]
for i in range(5):
    tim=Turtle()
    tim.shape('turtle')
    tim.color(colors[i])
    tim.penup()
    tim.goto(-300,ycor[i])
    turtle_list.append(tim)

turtle_list[4].goto(300,-300)
turtle_list[4].pendown()
turtle_list[4].goto(300,300)
turtle_list[4].penup()
turtle_list[4].goto(-300,-160)
user_bet=my_screen.textinput(title='tutle race',prompt='which color turtle will win the race?')
w_turtle=Turtle()
w_turtle.color("red")
w_turtle.hideturtle()
game_on=True
while game_on:
    for t in turtle_list:
        a = random.randint(10, 25)
        t.forward(a)
        if t.xcor() > 300:
            winner = t.pencolor()
            game_on = False
            if (user_bet == winner):
                w_turtle.write("you won ", font=("Arial", "14", "bold"))
            else:
                w_turtle.write("you lost....")

my_screen.exitonclick()