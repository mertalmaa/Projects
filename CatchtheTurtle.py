import random
import turtle


#screen
game_screen = turtle.Screen()
game_screen.bgcolor("black")
game_screen.title("Catch the Turtle")

#important information
FONT = ("Arial", 20, "normal")
top_height = game_screen.window_height()/2*0.89
grid_size = 10.5
number_list = [-20,-10,0,10,20]
score = 0
turtle_list = list()
still_running = True

#timer turtle
timer_turtle = turtle.Turtle()

#score turtle
score_turtle = turtle.Turtle()
score_turtle.ht()
score_turtle.pencolor("white")
score_turtle.penup()
score_turtle.goto(0,top_height)
score_turtle.write(f"Score: {score}", align="center", font=FONT)

def make_turtle(x, y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    t.color("white")
    t.shapesize(2.3)
    t.goto(x*grid_size, y*grid_size)
    turtle_list.append(t)
    def detect_turtle(x,y):
        game_screen.delay(0)
        global score
        score_turtle.clear()
        score += 1
        score_turtle.write(f"Score: {score}", align="center", font=FONT)
    t.onclick(detect_turtle)


def setup_turtles():
    for x in number_list:
        for y in number_list:
            make_turtle(x, y)

def hide_turtles():
    for x in turtle_list:
        x.hideturtle()

def random_turtle():
    global still_running
    if still_running:
        hide_turtles()
        random.choice(turtle_list).showturtle()
        game_screen.ontimer(random_turtle, 1000)
#time = 30
def timer(time):
    global still_running
    #global time
    game_screen.delay(0)
    timer_turtle.ht()
    timer_turtle.penup()
    timer_turtle.pencolor("white")
    timer_turtle.goto(0,top_height-30)
    if time >= 0:
        timer_turtle.clear()
        timer_turtle.write(f"Game Time: {time}", align="center", font=FONT)
        game_screen.ontimer(lambda: timer(time-1), 1000)
    else:
        still_running = False
        timer_turtle.clear()
        timer_turtle.goto(0,25)
        timer_turtle.write("Game Over", align="center", font=FONT)
        score_turtle.clear()
        score_turtle.goto(0,-25)
        score_turtle.write(f"Result Score: {score}", align="center",font= FONT)
        hide_turtles()

game_screen.tracer(0)

setup_turtles()
random_turtle()
timer(10)

game_screen.tracer(1)

turtle.mainloop()