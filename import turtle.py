
import time
import random
import turtle

delay = 0.1
body_segments = []

#WINDOW CONFIGURATION
wn = turtle.Screen()
wn.setup(width=600, height=600)
wn.title("snake game")
wn.bgcolor("light green")

#HEAD CONFIGURATION
head = turtle.Turtle()
head.color("green")
head.speed(0)
head.goto(0, 0)
head.penup()
head.shape("square")
head.direction = "stop"

#FOOD CONFIGURATION
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0,100)
food.direction = "stop"

#TEXT CONFIGURATION
score = 0
high_score = 0

texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0     High Score: 0", align = "center", font =("Courier", 24, "normal"))

#MOVEMENT DEFINITION
def mov():
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
        
    if head.direction == "pause":
        x = head.xcor()
        y = head.ycor()
        head.setx(x)
        head.sety(y)

#MOVEMENT DIRECTION DEFINITION
def dirUp():
    head.direction = "up"
def dirDown():
    head.direction = "down"
def dirLeft():
    head.direction = "left"
def dirRight():
    head.direction = "right"
def pause():
    head.direction = "stop"

#KEYBOARD MOVEMENT SYNC
wn.listen()
wn.onkeypress(dirUp, "Up")
wn.onkeypress(dirDown, "Down")
wn.onkeypress(dirLeft, "Left")
wn.onkeypress(dirRight, "Right")
wn.onkeypress(pause, "P")

while True:
    wn.update()
   
    #HEAD VS WINDOWS
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        #HIDE SEGMENTS
        for segment in body_segments:
            segment.goto(1000, 1000)    
        
        body_segments.clear()
        
        score = 0
        texto.clear()   
        texto.write("Score: {}     High Score: {}".format(score, high_score), 
            align = "center", font =("Courier", 24, "normal"))
    
    #HEAD VS FOOD
    if head.distance(food) < 20:
       
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x,y)

        #SEGMENT CONFIG
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        body_segments.append(new_segment)

        score += 1
         
        if score > high_score: 
            high_score = score 

        texto.clear()   
        texto.write("Score: {}    High Score: {}".format(score, high_score), 
          align = "center", font =("Courier", 24, "normal"))

    totalSeg = len(body_segments)

    for i in range(totalSeg - 1, 0, -1):
        x = body_segments[i-1].xcor()
        y = body_segments[i-1].ycor()
        body_segments[i].goto(x, y)


    if totalSeg > 0:
        x = head.xcor()
        y = head.ycor()
        body_segments[0].goto(x, y)

    mov()

    #BODY COLLIDE
    for segment in body_segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            #HIDE SEGMENTS
            for segment in body_segments:
                segment.goto(1000, 1000)  
          
            body_segments.clear()

            score = 0
            texto.clear()   
            texto.write("Score: {}    High Score: {}".format(score, high_score), 
              align = "center", font =("Courier", 24, "normal"))



    time.sleep(delay)

turtle.done()
