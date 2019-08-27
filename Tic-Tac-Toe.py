from turtle import *
from random import randint
bgcolor('black')
screen = Screen()
count = 0
Players_turn = 0
board = list()
def draw_cross (x,y):
    global board
    cross = Turtle()
    cross.color("red")
    cross.hideturtle()
    cross.penup()
    cross.pensize(7)
    if ((x >= -95 and x <= 95) and y >= 105): #vasat bala    
        cross.goto(95,106)
        cross.pendown()
        cross.goto(-95,294)
        cross.penup()
        cross.goto(95,294)
        cross.pendown()
        cross.goto(-95,106)
        board.append('2X')
    elif ((x >= 105 and x <= 300) and y >= 105):  #bala gooshe rast  
        cross.goto(296,106)
        cross.pendown()
        cross.goto(106,296)
        cross.penup()
        cross.goto(296,296)
        cross.pendown()
        cross.goto(106,106)
        board.append('3X')
    elif ((x >= -300 and x <= -105) and y >= 105):    #bala gooshe chap
        cross.goto(-107 ,106)
        cross.pendown()
        cross.goto(-295,296)
        cross.penup()
        cross.goto(-107,296)
        cross.pendown()
        cross.goto(-295,106)
        board.append('1X')
    elif ((x >= -300 and x <= -105) and (y >= -95 and y <= 95)):  #vasat chap   
        cross.goto(-107,-93)
        cross.pendown()
        cross.goto(-295,93)
        cross.penup()
        cross.goto(-107,93)
        cross.pendown()
        cross.goto(-295,-93)
        board.append('4X')
    elif ((x >= -300 and x <= -105) and (y <= -105 and y >= -300)):    #paein gooshe chap
        cross.goto(-107,-295)
        cross.pendown()
        cross.goto(-295,-107)
        cross.penup()
        cross.goto(-107,-107)
        cross.pendown()
        cross.goto(-295,-295)
        board.append('7X')
    elif ((x >= -95 and x <= 95) and (y <= -105 and y >= -300)):    # vasat paein
        cross.goto(95,-295)
        cross.pendown()
        cross.goto(-95,-107)
        cross.penup()
        cross.goto(95,-107)
        cross.pendown()
        cross.goto(-95,-295)
        board.append('8X')
    elif ((x >= -95 and x <= 95) and (y <= 95 and y >= -95)):    #vasat
        cross.goto(95,-93)
        cross.pendown()
        cross.goto(-95,93)
        cross.penup()
        cross.goto(95,93)
        cross.pendown()
        cross.goto(-95,-93)
        board.append('5X')
    elif ((x >= 105 and x <= 300) and (y >= -95 and y <= 95)):    #vasat rast
        cross.goto(296,-93)
        cross.pendown()
        cross.goto(106,93)
        cross.penup()
        cross.goto(296,93)
        cross.pendown()
        cross.goto(106,-93)
        board.append('6X')
    elif ((x >= 105 and x <= 300) and (y <= -105 and y >= -300)):    #paein gooshe rast
        cross.goto(296,-295)
        cross.pendown()
        cross.goto(106,-107)
        cross.penup()
        cross.goto(296,-107)
        cross.pendown()
        cross.goto(106,-295)
        board.append('9X')    
                
def draw_circle (x,y):
    global board
    circle = Turtle()
    circle.color("blue")
    circle.hideturtle()
    circle.penup()
    circle.pensize(7)
    if ((x >= -95 and x <= 95) and y >= 105): #vasat bala    
        circle.goto(0,106)
        circle.pendown()
        circle.circle(92)
        board.append('O2')
    elif ((x >= 105 and x <= 300) and y >= 105):  #bala gooshe rast  
        circle.goto(200,106)
        circle.pendown()
        circle.circle(92)
        board.append('O3')
    elif ((x >= -300 and x <= -105) and y >= 105):    #bala gooshe chap
        circle.goto(-200 ,106)
        circle.pendown()
        circle.circle(92)
        board.append('O1')
    elif ((x >= -300 and x <= -105) and (y >= -95 and y <= 95)):  #vasat chap   
        circle.goto(-200,-90)
        circle.pendown()
        circle.circle(92)
        board.append('O4')
    elif ((x >= -300 and x <= -105) and (y <= -105 and y >= -300)):    #paein gooshe chap
        circle.goto(-200,-290)
        circle.pendown()
        circle.circle(92)
        board.append('O7')
    elif ((x >= -95 and x <= 95) and (y <= -105 and y >= -300)):    # vasat paein
        circle.goto(0,-290)
        circle.pendown()
        circle.circle(92)
        board.append('O8')
    elif ((x >= -95 and x <= 95) and (y <= 95 and y >= -95)):    #vasat
        circle.goto(0,-90)
        circle.pendown()
        circle.circle(92)
        board.append('O5')
    elif ((x >= 105 and x <= 300) and (y >= -95 and y <= 95)):    #vasat rast
        circle.goto(200,-90)
        circle.pendown()
        circle.circle(92)
        board.append('O6')
    elif ((x >= 105 and x <= 300) and (y <= -105 and y >= -300)):    #paein gooshe rast
        circle.goto(200,-290)
        circle.pendown()
        circle.circle(92)
        board.append('O9')
def cross_win_anouncement():
    text = Turtle()
    screen.clear()
    text.pu()
    text.color('red')
    text.write("Player One Won!!!!" , True , align = 'center' , font = ('Arial' , 36 , 'normal'))


def circle_win_anouncement():
    text = Turtle()
    screen.clear()
    text.pu()
    text.color('blue')
    text.write("Player Two Won!!!!", True, align='center',
               font=('Arial', 36, 'normal'))




    




def clicked (x,y):
    global Players_turn , board , count
    draw_line = Turtle()
    draw_line.hideturtle()
    draw_line.penup()
    draw_line.pensize(8)
    draw_line.color('Gold')
    if (count <= 8):
        if (count >= 4):
            if ('1X' in board and '2X' in board and '3X' in board) == True:
                draw_line.goto(-300,200)
                draw_line.pendown()
                draw_line.goto(300,200)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('1X' in board and '4X' in board and '7X' in board) == True:
                draw_line.goto(-200,300)
                draw_line.pendown()
                draw_line.goto(-200,-300)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('1X' in board and '5X' in board and '9X' in board) == True:
                draw_line.goto(-300,300)
                draw_line.pendown()
                draw_line.goto(300,-300)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('3X' in board and '6X' in board and '9X' in board) == True:
                draw_line.goto(200,300)
                draw_line.pendown()
                draw_line.goto(200,-300)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('3X' in board and '5X' in board and '7X' in board) == True:
                draw_line.goto(300,300)
                draw_line.pendown()
                draw_line.goto(-300,-300)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('2X' in board and '5X' in board and '8X' in board) == True:
                draw_line.goto(-200,300)
                draw_line.pendown()
                draw_line.goto(-200,-300)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('8X' in board and '9X' in board and '7X' in board) == True:
                draw_line.goto(-300,-200)
                draw_line.pendown()
                draw_line.goto(300,-200)
                cross_win_anouncement()
                screen.exitonclick()
            elif ('6X' in board and '4X' in board and '5X' in board) == True:
                draw_line.goto(-300,0)
                draw_line.pendown()
                draw_line.goto(300,0)
                cross_win_anouncement()
                screen.exitonclick()                            
            elif ('O1' in board and 'O2' in board and 'O3' in board) == True:
                draw_line.goto(-300,200)
                draw_line.pendown()
                draw_line.goto(300,200)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O1' in board and 'O4' in board and 'O7' in board) == True:
                draw_line.goto(-200,300)
                draw_line.pendown()
                draw_line.goto(-200,-300)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O1' in board and 'O5' in board and 'O9' in board) == True:
                draw_line.goto(-300,300)
                draw_line.pendown()
                draw_line.goto(300,-300)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O9' in board and 'O6' in board and 'O3' in board) == True:
                draw_line.goto(200,300)
                draw_line.pendown()
                draw_line.goto(200,-300)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O3' in board and 'O5' in board and 'O7' in board) == True:
                draw_line.goto(300,300)
                draw_line.pendown()
                draw_line.goto(-300,-300)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O4' in board and 'O5' in board and 'O6' in board) == True:
                draw_line.goto(-300,0)
                draw_line.pendown()
                draw_line.goto(300,0)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O5' in board and 'O2' in board and 'O8' in board) == True:
                draw_line.goto(-200,300)
                draw_line.pendown()
                draw_line.goto(-200,-300)
                circle_win_anouncement()
                screen.exitonclick()
            elif ('O7' in board and 'O8' in board and 'O9' in board) == True:
                draw_line.goto(-300,-200)
                draw_line.pendown()
                draw_line.goto(300,-200)
                circle_win_anouncement()
                screen.exitonclick()                            

            else:
                if (Players_turn == 0):
                    Players_turn = 1
                    count += 1
                    draw_circle(x,y)
                else:
                    Players_turn = 0
                    count += 1
                    draw_cross(x,y)
        else:
            if (Players_turn == 0):
                Players_turn = 1
                count += 1
                draw_circle(x,y)
            else:
                Players_turn = 0
                count += 1
                draw_cross(x,y)
    else:
        if ('1X' in board and '2X' in board and '3X' in board) == True:
            draw_line.goto(-300,200)
            draw_line.pendown()
            draw_line.goto(300,200)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('1X' in board and '4X' in board and '7X' in board) == True:
            draw_line.goto(-200,300)
            draw_line.pendown()
            draw_line.goto(-200,-300)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('1X' in board and '5X' in board and '9X' in board) == True:
            draw_line.goto(-300,300)
            draw_line.pendown()
            draw_line.goto(300,-300)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('3X' in board and '6X' in board and '9X' in board) == True:
            draw_line.goto(200,300)
            draw_line.pendown()
            draw_line.goto(200,-300)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('3X' in board and '5X' in board and '7X' in board) == True:
            draw_line.goto(300,300)
            draw_line.pendown()
            draw_line.goto(-300,-300)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('2X' in board and '5X' in board and '8X' in board) == True:
            draw_line.goto(-200,300)
            draw_line.pendown()
            draw_line.goto(-200,-300)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('8X' in board and '9X' in board and '7X' in board) == True:
            draw_line.goto(-300,-200)
            draw_line.pendown()
            draw_line.goto(300,-200)
            cross_win_anouncement()
            screen.exitonclick()
        elif ('6X' in board and '4X' in board and '5X' in board) == True:
            draw_line.goto(-300,0)
            draw_line.pendown()
            draw_line.goto(300,0)
            cross_win_anouncement()
            screen.exitonclick()                            
        elif ('O1' in board and 'O2' in board and 'O3' in board) == True:
            draw_line.goto(-300,200)
            draw_line.pendown()
            draw_line.goto(300,200)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O1' in board and 'O4' in board and 'O7' in board) == True:
            draw_line.goto(-200,300)
            draw_line.pendown()
            draw_line.goto(-200,-300)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O1' in board and 'O5' in board and 'O9' in board) == True:
            draw_line.goto(-300,300)
            draw_line.pendown()
            draw_line.goto(300,-300)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O9' in board and 'O6' in board and 'O3' in board) == True:
            draw_line.goto(200,300)
            draw_line.pendown()
            draw_line.goto(200,-300)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O3' in board and 'O5' in board and 'O7' in board) == True:
            draw_line.goto(300,300)
            draw_line.pendown()
            draw_line.goto(-300,-300)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O4' in board and 'O5' in board and 'O6' in board) == True:
            draw_line.goto(-300,0)
            draw_line.pendown()
            draw_line.goto(300,0)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O5' in board and 'O2' in board and 'O8' in board) == True:
            draw_line.goto(-200,300)
            draw_line.pendown()
            draw_line.goto(-200,-300)
            circle_win_anouncement()
            screen.exitonclick()
        elif ('O7' in board and 'O8' in board and 'O9' in board) == True:
            draw_line.goto(-300,-200)
            draw_line.pendown()
            draw_line.goto(300,-200)
            circle_win_anouncement()
            screen.exitonclick() 
        else:
            screen.clear()
            draw_line.write("Draw!!!!" , True , align = 'center' , font = ('Arial' , 24 , 'normal'))    
            screen.exitonclick()






    
setup(600,600)
first_vertical_line = Turtle()
second_vertical_line = Turtle()
first_horizontal_line = Turtle()
second_horizontal_line = Turtle()
first_vertical_line.hideturtle()
second_vertical_line.hideturtle()
first_horizontal_line.hideturtle()
second_horizontal_line.hideturtle()
first_vertical_line.pensize(10)
second_vertical_line.pensize(10)
first_horizontal_line.pensize(10)
second_horizontal_line.pensize(10)
first_vertical_line.color('white')
second_vertical_line.color('white')
first_horizontal_line.color('white')
second_horizontal_line.color('white')
circle = Turtle()
circle.shape("circle")
circle.color("blue")
circle.hideturtle()
circle.penup() 
first_horizontal_line.pu()
second_horizontal_line.pu()
first_vertical_line.pu()
second_vertical_line.pu()
first_horizontal_line.goto(-100,300)
second_horizontal_line.goto(100,300)
first_vertical_line.goto(-300,100)
second_vertical_line.goto(-300,-100)
first_horizontal_line.pd()
second_horizontal_line.pd()
first_vertical_line.pd()
second_vertical_line.pd()
first_horizontal_line.goto(-100,-300)
second_horizontal_line.goto(100,-300)
first_vertical_line.goto(300,100)
second_vertical_line.goto(300,-100)
first_horizontal_line = penup()
second_horizontal_line = penup()
first_vertical_line = penup()
second_vertical_line = penup()
onscreenclick(clicked)
mainloop()

