from turtle import *
from random import randint
import time

screen = Screen()
#building frog game
screen.setup(450, 450)


#///////////////////////
frog = Turtle()
frog.color('Light Green')
frog.shape('triangle')
frog.speed(0)
frog.hideturtle()
frog.pu()
frog.goto(0, -185)
frog.setheading(90)
frog.showturtle()
frog.direction = "stop"
#///////////////////
car = Turtle()
car2 = Turtle()
car3 = Turtle()
car4 = Turtle()
car5 = Turtle()
car6 = Turtle()
car.shape('square')
car2.shape('square')
car3.shape('square')
car4.shape('square')
car5.shape('square')
car6.shape('square')
car.pu()
car2.pu()
car3.pu()
car4.pu()
car5.pu()
car6.pu()
car.hideturtle()
car2.hideturtle()
car3.hideturtle()
car4.hideturtle()
car5.hideturtle()
car6.hideturtle()
car.goto(-215, 215)  # setting up the cars to hit the frog :)
car2.goto(-165, 175)
car3.goto(-185, 95)
car4.goto(-185, -20)
car5.goto(-195, -75)
car6.goto(-205, -115)
car.showturtle()
car2.showturtle()
car3.showturtle()
car4.showturtle()
car5.showturtle()
car6.showturtle()
#/////////////////////


def up():
    frog.setheading(90)
    frog.direction = 'up'


def down():
    frog.setheading(270)
    frog.direction = 'down'


def left():
    frog.setheading(180)
    frog.direction = 'left'


def right():
    frog.setheading(0)
    frog.direction = 'right'


def movement():
    if frog.direction == 'up':
        y = frog.ycor()
        frog.sety(y+1)
    elif frog.direction == 'down':
        y = frog.ycor()
        frog.sety(y-1)
    elif frog.direction == 'right':
        x = frog.xcor()
        frog.setx(x+1)
    elif frog.direction == 'left':
        x = frog.xcor()
        frog.setx(x-1)

        #x = frog.xcor()
        #y = frog.ycor()
        #frog.setpos(x,y)


screen.listen()
screen.onkeypress(up, 'w')
screen.onkeypress(left, 'a')
screen.onkeypress(down, 's')
screen.onkeypress(right, 'd')
#wscreen.onkeypress(jump , 'j')
screen.tracer(0)  # holding the animation

while True:
    screen.update()  # for updating the screen
    car.forward(5)
    car2.forward(5)
    car3.forward(5)
    car4.forward(5)
    car5.forward(5)
    car6.forward(5)
    if (car.xcor() >= 215):
        car.hideturtle()
        car.setposition(-215, randint(176, 215))
        car.showturtle()
    elif (car2.xcor() >= 215):
        car2.hideturtle()
        car2.setposition(-165, randint(96, 175))
        car2.showturtle()
    elif (car3.xcor() >= 215):
        car3.hideturtle()
        car3.setposition(-185, randint(-19, 95))
        car3.showturtle()
    elif (car4.xcor() >= 215):
        car4.hideturtle()
        car4.setposition(-185, randint(-74, -20))
        car4.showturtle()
    elif (car5.xcor() >= 215):
        car5.hideturtle()
        car5.setposition(-195, randint(-135, -75))
        car5.showturtle()
    elif (car6.xcor() >= 290):
        car6.hideturtle()
        car6.setposition(-205, randint(-155, -135))
        car6.showturtle()
    if (frog.distance(car) < 20):
        screen.clear()
        car.setpos(0, 0)
        car.color('red')
        car.write("You Lost !!!", True, align='center',
                  font=('Arial', 36, 'normal'))
        screen.exitonclick()
    elif (frog.distance(car2) < 20):
        screen.clear()
        car.setpos(0, 0)
        car.color('red')
        car.write("You Lost !!!", True, align='center',
                  font=('Arial', 36, 'normal'))
        screen.exitonclick()
    elif (frog.distance(car3) < 20):
        screen.clear()
        car.setpos(0, 0)
        car.color('red')
        car.write("You Lost !!!", True, align='center',
                  font=('Arial', 36, 'normal'))
        screen.exitonclick()
    elif (frog.distance(car4) < 20):
        screen.clear()
        car.setpos(0, 0)
        car.color('red')
        car.write("You Lost !!!", True, align='center',
                  font=('Arial', 36, 'normal'))
        screen.exitonclick()
    elif (frog.distance(car5) < 20):
        screen.clear()
        car.setpos(0, 0)
        car.color('red')
        car.write("You Lost !!!", True, align='center',
                  font=('Arial', 36, 'normal'))
        screen.exitonclick()
    elif (frog.distance(car6) < 20):
        screen.clear()
        car.setpos(0, 0)
        car.color('red')
        car.write("You Lost !!!", True, align='center',
                  font=('Arial', 36, 'normal'))
        screen.exitonclick()
    if (frog.ycor() >= 215):
        frog.hideturtle()
        frog.setpos(randint(-215, 215), -185)
        frog.showturtle()

    movement()
    time.sleep(0.015)


screen.mainloop()
