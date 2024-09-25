# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0


# The window screen
wn = turtle.Screen()
wn.title("A Snake Game")
wn.bgcolor("#006633") 

wn.setup(width=600, height=600) # The width and height of the screen

wn.cv._rootwindow.resizable(False, False) # disable window resize

wn.tracer(0)  # set delay for update drawings

# head of the snake
head = turtle.Turtle()
head.shape("circle")
head.color("white")
head.penup()  # stop drawing lines when moving
head.speed(0)
head.goto(0, 0)
head.direction = "Stop"

# food of the Snake
food = turtle.Turtle()
colors = random.choice(["red", "#808080", "#FF8000"])
shapes = random.choice(["circle"])
food.shape(shapes)
food.color(colors)
food.penup() 
food.speed(0)
food.goto(0, 100)

# View the Score
pen = turtle.Turtle()
pen.shape("square")
pen.color("white")
pen.penup()
pen.speed(0)
pen.goto(0, 250)
pen.hideturtle()
pen.write("Score: 0   Top Score: 0", align="center", font=("Arial", 24, "bold"))


# assigning key directions
def goUp():
    if head.direction != "down":
        head.direction = "up"


def goDown():
    if head.direction != "up":
        head.direction = "down"


def goLeft():
    if head.direction != "right":
        head.direction = "left"


def goRight():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)


# key binding
wn.listen()
wn.onkeypress(goUp, "w")
wn.onkeypress(goDown, "s")
wn.onkeypress(goLeft, "a")
wn.onkeypress(goRight, "d")

segments = []


# Main Gameplay
while True:
    wn.update()

    # First: Checking the head with borders
    if (
        head.xcor() > 290
        or head.xcor() < -290
        or head.ycor() > 290
        or head.ycor() < -290
    ):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
       
        food.shape(shapes)
        food.color(colors)
        for segment in segments:
            segment.goto(1000, 1000)
            segment.hideturtle()
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write( "Score:{}  Top Score:{}".format(score, high_score),align="center",font=("Arial", 24, "bold"),)


    # Second: Checking the head with food
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)

        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.shape("circle")
        new_segment.color(food.color()[0])  # tail colour
        new_segment.speed(0)
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001  # increase game difficulty
        score += 5
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}   Top Score: {} ".format(score, high_score),align="center",font=("Arial", 24, "bold"),)


    # Move all snake body then move the (head)
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    # Checking for head collisions with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            food.shape(shapes)
            food.color(colors)
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}   Top Score: {} ".format(score, high_score),align="center",font=("Arial", 24, "bold"), )
    
    time.sleep(delay)
