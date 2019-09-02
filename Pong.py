from turtle import *
from random import randint
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(800,500)
action_move = list()
A_Score = 0
B_Score = 0

degree = [0,25,155,180,205,335]

#initializing paddle a
paddle_a = Turtle()
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.hideturtle()
paddle_a.pu()
paddle_a.speed(0)
paddle_a.shapesize(stretch_len = 5)
paddle_a.setheading(90)
paddle_a.goto(-350,0)
paddle_a.showturtle()
paddle_a.direction = 'stop'

#initializing paddle b
paddle_b = Turtle()
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.hideturtle()
paddle_b.pu()
paddle_b.speed(0)
paddle_b.shapesize(stretch_len=5)
paddle_b.setheading(90)
paddle_b.goto(350, 0)
paddle_b.showturtle()
paddle_b.direction = 'stop'


#initializing the ball
ball = Turtle()
ball.shape('square')
ball.color('white')
ball.pu()

#///////////////////////////
def paddle_a_up():
    paddle_a.direction = 'up'

def paddle_a_down():
    paddle_a.direction = 'down'


def paddle_b_up():
    paddle_b.direction = 'up'


def paddle_b_down():
    paddle_b.direction = 'down'




#//////////////////////////
def paddle_a_movement():
    if paddle_a.direction == 'up':
        y = paddle_a.ycor()
        paddle_a.sety(y+5)
    elif paddle_a.direction == 'down':
        y = paddle_a.ycor()
        paddle_a.sety(y-5)
    
def paddle_b_movement():
    if paddle_b.direction == 'up':
        y = paddle_b.ycor()
        paddle_b.sety(y+5)
    elif paddle_b.direction == 'down':
        y = paddle_b.ycor()
        paddle_b.sety(y-5)





screen.listen()
screen.onkeypress(paddle_a_up , 'w')
screen.onkeypress(paddle_a_down , 's')
screen.onkeypress(paddle_b_up , '8')
screen.onkeypress(paddle_b_down , '2')

def setheading_ball():
    ball.setheading(degree[randint(0,5)])

paddle_a_score_counter = Turtle()
paddle_a_score_counter.pu()
paddle_a_score_counter.hideturtle()
paddle_a_score_counter.color('white')
paddle_a_score_counter.goto(-350,220)
paddle_a_score_counter.write(
    "Player B Score: " + str(B_Score), True, align='center')

paddle_b_score_counter = Turtle()
paddle_b_score_counter.pu()
paddle_b_score_counter.color('white')
paddle_b_score_counter.hideturtle()
paddle_b_score_counter.goto(350,220)
#paddle_b_score_counter.showturtle()
paddle_b_score_counter.write(
    "Player B Score: " + str(B_Score), True, align='center')









setheading_ball()
screen.tracer(0)

while True:
    screen.update()
    for i in range(5):
        ball.forward(1)
        time.sleep(0.003)
    if (ball.xcor() > 400):
        A_Score += 1
        paddle_a_score_counter.undo()
        paddle_a_score_counter.goto(-350,220)
        paddle_a_score_counter.write("Player A Score: " + str(A_Score) , True , align = 'center')
        #paddle_a_score()
        ball.home()
        setheading_ball()
    elif (ball.xcor() < -400):
        B_Score += 1
        paddle_b_score_counter.undo()
        paddle_b_score_counter.write("Player B Score: " + str(B_Score) , True , align = 'center')
        #paddle_b_score()
        ball.home()
        setheading_ball()

    if (paddle_a.distance(ball)) < 28 :
        if (paddle_a.ycor() > 180 and paddle_a.ycor() < 240) :
            action_move.append('A')
            ball.setheading(45)
            for i in range (2) :
                ball.forward(1)
        elif (paddle_a.ycor() > 120 and paddle_a.ycor() < 180 ) :
            action_move.append('A')
            ball.setheading(45)
            for i in range (3) :
                ball.forward(1)
            
        elif (paddle_a.ycor() > 60 and paddle_a.ycor() < 120) :
            action_move.append('A')
            ball.setheading(35)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_a.ycor() >= 0 and paddle_a.ycor() <= 15):
            action_move.append('A')
            ball.setheading(0)
            for i in range(2):
                ball.forward(1)
        elif (paddle_a.ycor() > 0 and paddle_a.ycor() < 60) :
            action_move.append('A')
            ball.setheading(25)
            for i in range (3) :
                ball.forward(1)    
        elif (paddle_a.ycor() > -60 and paddle_a.ycor() < 0) :
            action_move.append('A')
            ball.setheading(15)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_a.ycor() > -120 and paddle_a.ycor() < -60) :
            action_move.append('A')
            ball.setheading(45)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_a.ycor() > -180 and paddle_a.ycor() < -120):
            action_move.append('A')
            ball.setheading(315)
            for i in range(3):
                ball.forward(1)
        elif (paddle_a.ycor() > -240 and paddle_a.ycor() < -180):
            action_move.append('A')
            ball.setheading(315)
            for i in range(3):
                ball.forward(1)
    if (paddle_b.distance(ball)) < 28 :
        if (paddle_b.ycor() > 180 and paddle_b.ycor() < 240) :
            action_move.append('B')
            ball.setheading(225)
            for i in range (2) :
                ball.forward(1)
        elif (paddle_b.ycor() > 120 and paddle_b.ycor() < 180 ) :
            action_move.append('B')
            ball.setheading(225)
            for i in range (3) :
                ball.forward(1)
            
        elif (paddle_b.ycor() > 60 and paddle_b.ycor() < 120) :
            action_move.append('B')
            ball.setheading(215)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_b.ycor() > 0 and paddle_b.ycor() < 60) :
            action_move.append('B')
            ball.setheading(205)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_b.ycor() >= 0 and paddle_b.ycor() <= 15) :
            action_move.append('B')
            ball.setheading(180)
            for i in range (2) :
                ball.forward(1)        
        elif (paddle_b.ycor() > -60 and paddle_b.ycor() < 0) :
            action_move.append('B')
            ball.setheading(195)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_b.ycor() > -120 and paddle_b.ycor() < -60) :
            action_move.append('B')
            ball.setheading(225)
            for i in range (3) :
                ball.forward(1)
        elif (paddle_b.ycor() > -180 and paddle_b.ycor() < -120):
            action_move.append('B')
            ball.setheading(135)
            for i in range(3):
                ball.forward(1)
        elif (paddle_b.ycor() > -240 and paddle_b.ycor() < -180):
            action_move.append('B')
            ball.setheading(135)
            for i in range(3):
                ball.forward(1)
    if (ball.ycor() >= 235) :
        if (action_move[-1] == 'A') :
            if (ball.xcor() >= 0) :
                ball.setheading(305)
                ball.forward(2)
            elif (ball.xcor() < 0):
                ball.setheading(325)
                ball.forward(2) 
        elif (action_move[-1] == 'B'):
            if (ball.xcor() >= 0):
                ball.setheading(225)
                ball.forward(2)
            elif (ball.xcor() < 0):
                ball.setheading(250)
                ball.forward(2)
    elif (ball.ycor() <= -235) :
        if (action_move[-1] == 'B') :
            if (ball.xcor() >= 0) :
                ball.setheading(165)
                ball.forward(2)
            elif (ball.xcor() < 0) :
                ball.setheading(140)    
                ball.forward(2)
        elif (action_move[-1] == 'A'):
            if (ball.xcor() < 0):
                ball.setheading(45)
                ball.forward(2)






    paddle_a_movement()
    paddle_b_movement()
    time.sleep(0.004)




screen.mainloop()
