import turtle
from turtle import*
t=Turtle()
screen = turtle.Screen()
screen.bgcolor("#AAAAFF")
screen.setup(width = 1.0, height = 1.0)
 

def draw_circle(size,color):
    t.pendown()
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    t.penup()
def draw_triangle(size,color):
    t.setheading(0)
    t.color(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.fd(size)
        t.lt(120)
    t.end_fill()
 
######### Cristmas tree end here ########
# # Creating Right half of the tree
# t.begin_fill()
# t.fillcolor("green")
# t.forward(200)
# t.left(150)
# t.forward(180)
# t.right(150)
# t.forward(110)
# t.left(150)
# t.forward(140)
# t.right(150)
# t.forward(80)
# t.left(150)
# t.forward(130)
# t.end_fill()

# #left half of the tree
# t.begin_fill()
# t.fillcolor("green")
# t.left(60)
# t.forward(130)
# t.left(150)
# t.forward(80)
# t.right(150)
# t.forward(140)
# t.left(150)
# t.forward(110)
# t.right(150)
# t.forward(180)
# t.left(150)
# t.forward(200)
# t.end_fill()

# #Creating the trunck of the tree
# t.penup()
# t.color("brown")
# t.goto(20,0)
# t.begin_fill()
# t.right(90)
# t.forward(80)
# t.right(90)
# t.forward(40)
# t.right(90)
# t.forward(80)
# t.end_fill()

# #Creating the balls on the Christmas Tree
# t.goto(120,-10)
# draw_circle(10,"red")

# t.goto(210,-10)
# draw_circle(10,"blue")

# t.goto(-100,-10)
# draw_circle(10,"red")

# t.goto(-185,-10)
# draw_circle(10,"blue")

# t.goto(160,80)
# draw_circle(10,"yellow")

# t.goto(-145,80)
# draw_circle(10,"yellow")

# t.goto(120,150)
# draw_circle(10,"red")

# t.goto(-100,150)
# draw_circle(10,"red")

# t.goto(5,25)
# draw_circle(7,"yellow")

# t.goto(5,90)
# draw_circle(7,"red")

# t.goto(5,160)
# draw_circle(7,"blue")

# #Drawing the bells using triangle.
# t.goto(-80,30)
# draw_triangle(15,"yellow")

# t.goto(70,30)
# draw_triangle(15,"red")

# t.goto(-50,110)
# draw_triangle(15,"blue")

# t.goto(30,110)
# draw_triangle(15,"yellow")

# # Printing the star using for loop
# t.penup()
# t.color("yellow")
# t.goto(-20,240)
# t.begin_fill()
# t.pendown()
# for i in range(5):
#     t.forward(40)
#     t.right(144)
# t.end_fill()

####### Cristmas tree end here ########

####Draw hallowen Pumpkin start#####
# t.penup()
# t.pensize(2)
# t.goto(-500,-300)
# draw_circle(150,"orange")
# t.goto(-580,-300)
# draw_circle(150,"orange")

# t.goto(-650,-100)
# draw_triangle(50,"red")
# t.goto(-480,-100)
# draw_triangle(50,"red")
# t.goto(-560,-170)
# draw_triangle(40,"red")

# t.goto(-570,-20)
# draw_triangle(50,"green")
# t.goto(-555,0)
# t.color("green")
# t.fillcolor("green")
# t.begin_fill()
# t.fd(20)
# t.lt(90)
# t.fd(40)
# t.lt(90)
# t.fd(20)
# t.lt(90)
# t.fd(40)
# t.end_fill()

# t.goto(-625,-240)
# for i in range(8):
#     draw_triangle(25,"red")
#     t.fd(20)

# t.goto(-480,-215)
# for i in range(8):
#     t.color("red")
#     t.fillcolor("red")
#     t.begin_fill()
#     t.setheading(180)
#     for i in range(3):
#         t.fd(20)
#         t.lt(120)
#     t.fd(20)
#     t.end_fill()
#     # draw_triangle(20,"red")
####Draw hallowen Pumpkin end##### 
 
##### Draw Flag start ####
# t.penup()
# t.goto(350,0)
# t.color("#003594")
# t.fillcolor("#003594")
# t.begin_fill()
# t.pendown()
# t.forward(300)
# t.left(150)
# t.forward(230)
# t.right(150)
# t.forward(150)
# t.left(150)
# t.forward(290)
# t.left(120)
# t.forward(260)
# t.end_fill()
# t.penup()

t.setheading(0)
t.goto(360,10)
t.color("#DC143C")
t.fillcolor("#DC143C")
t.begin_fill()
t.pendown()
t.forward(255)
t.left(150)
t.forward(225)
t.right(150)
t.forward(145)
t.left(150)
t.forward(238)
t.left(120)
t.forward(230)
t.end_fill()
t.penup()

# Moon
t.setheading(0)
t.goto(400,135)
draw_circle(30,"white")
t.goto(400,145)
draw_circle(30,"#DC143C")

#sun
t.setheading(0)
t.goto(380,100)
t.color("white")
t.fillcolor("white")
t.begin_fill()
t.pendown()
for i in range(10):
    t.forward(60)
    t.right(120) 
t.end_fill()
t.penup()

#red DC143C
##### Draw flag end ####
t.hideturtle()
delay = input("Press enter to finish.")
