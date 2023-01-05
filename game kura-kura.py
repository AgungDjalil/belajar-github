from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
color = ["red","yellow","orange","pink","green","blue","purple"]
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? enter a color")
posty = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for index_turtle in range(0, 6):
    turtle = Turtle("turtle")
    turtle.color(color[index_turtle])
    turtle.penup()
    turtle.goto(x=-230, y=posty[index_turtle])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_turtles = turtle.pencolor()
            if user_bet == winning_turtles:
                print("You win")
            else:
                print("You lose")
        turtle.forward(random.randint(0, 10))


screen.exitonclick()