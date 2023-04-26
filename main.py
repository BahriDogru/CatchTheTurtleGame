import turtle
import random


turtle_screen = turtle.Screen()
turtle_screen.bgcolor("light green")
turtle_screen.title("Catch The Turtle")
score = 0
game_over = False

# PLAYER TURTLE
my_turtle = turtle.Turtle()

# SCORE BOARD
score_board_turtle = turtle.Turtle()

#COUNTDOWN TURTLE
count_down_turtle = turtle.Turtle()


def scoreBoard():
    # Score Board
    height = turtle_screen.window_height()
    turtle_position = height * 0.46

    score_board_turtle.penup()
    score_board_turtle.setpos(0, turtle_position)
    score_board_turtle.write(f"Score:{score}", False, "right", font=('Arial', 18, 'normal'))
    score_board_turtle.hideturtle()


def countDown(time):
    global game_over
    # CountDown
    height = turtle_screen.window_height()
    turtle_position = height * 0.43

    count_down_turtle.penup()
    count_down_turtle.setpos(0, turtle_position)
    count_down_turtle.write("Time:", False, "right", font=('Arial', 18, 'normal'))
    count_down_turtle.hideturtle()

    if time >0:
        count_down_turtle.clear()
        count_down_turtle.write(f"Time:{time}", False, "right", font=('Arial', 18, 'normal'))
        turtle_screen.ontimer(lambda: countDown(time - 1), 1000)
    else:
        game_over = True
        count_down_turtle.clear()
        count_down_turtle.write("GAME OVER!", False, "right", font=('Arial', 18, 'normal'))
        my_turtle.hideturtle()

def clicekleft(x,y):
    global score
    score +=1
    score_board_turtle.clear()
    score_board_turtle.write(f"Score:{score}", False, "right", font=('Arial', 18, 'normal'))
    # print(x,y)

def turtle_randomly():
    if not game_over:
        my_turtle.shape("turtle")
        my_turtle.shapesize(2, 2)
        my_turtle.color("yellow", "green")
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.setpos(random.randint(-400,400),random.randint(-400,400))
        my_turtle.showturtle()
        turtle_screen.ontimer(turtle_randomly,1000)


turtle_screen.tracer(0)
scoreBoard()
countDown(15)
turtle_randomly()
my_turtle.onclick(clicekleft)
turtle_screen.tracer(1)

turtle.mainloop()
