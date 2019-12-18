#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name Joshua Ike
#
#Date 12/10/19
#


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw-
#Space should clear the screen-
#o and p should make the pen grow grow and smaller-
#u should pick the pen up or put the pen down?
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
turtleshape= "circle"
turtlecolor= "yellow"
turtlesize = 2

player = trtl.Turtle(shape=turtleshape)
player.color(turtlecolor)
player.shapesize(turtlesize)
player.shapesize(turtlesize)
player.speed(0)
player.pensize(2)
player.pencolor("black")
Drawer = trtl.Turtle()
Drawer.ht()




#movement functions
def Up():
    player.setheading(90)
    player.forward(10)

def Down():
    player.setheading(270)
    player.forward(10)
    
def Left():
    player.setheading(180)
    player.forward(10)


def Right():
    player.setheading(0)
    player.forward(10)

def space():
    player.clear()


#color/drawing functions
#this function sets the pensize

#this funtion binds pen size growth to o
def o():
    player.pensize(6)
   
#this function binds pen size shrinking to p
def p():
    player.pensize(3)

def u():
    y = 0
    if y == 0:
        player.pendown()
        y = (y + 1)
    else:
        player.penup()
        y = (y - 0)    



#this function sets the pen to go up or down if u is pressed.

#the next set of functions will change pen color
def a():
    player.pencolor("green")

def s():
    player.pencolor("red")

def d():
    player.pencolor("blue")
            
def f():
    player.pencolor("orange")




#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(Right, "Right")
wn.onkeypress(Left, "Left")
wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onkeypress(space,"space")
wn.onkeypress(o,"o")
wn.onkeypress(p,"p")
wn.onkeypress(a,"a")
wn.onkeypress(s,"s")
wn.onkeypress(d,"d")
wn.onkeypress(f,"f")
wn.onkeypress(u,"u")
            

#listen
wn.listen()


#mainloop
wn.mainloop()