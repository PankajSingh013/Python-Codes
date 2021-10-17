from turtle import Turtle, Screen
import random


screen= Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet=screen.textinput(title='Make your guess', prompt='which turtle will win the race? Enter a color')
#print(user_bet)

colors= ['red','black','blue','yellow','violet']
y_pos=[-70,-40,-10,20,50]
turtle_list=[]

# Creating 5 turtle objects and storing them in a list
for item_index in range(0,5):
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[item_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[item_index])
    turtle_list.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor()>230:
            is_race_on=False
            if turtle.pencolor()==user_bet:
                print(f'You Won! Winning color is {turtle.pencolor()}')
            else:
                print(f'You loose!!! Winning color is {turtle.pencolor()}')

        random_distance= random.randint(0,10)
        turtle.forward(random_distance)





screen.exitonclick()