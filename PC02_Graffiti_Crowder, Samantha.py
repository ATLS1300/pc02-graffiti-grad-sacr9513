#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Sammie Crowder
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======

up()

forward(50)

left(90)

forward(125)

dot(50)

color('red')

dot(25)

up()

left(90)

forward(90)

color('black')

dot(75)

color('red')

dot(25)

forward(90)

left(90)

forward(40)

shape('square')

circle(40, 50)

down()

width(10)

forward(50)

up()

forward(100)

down()

clearstamps()

shape('triangle')

stamp()

left(45)

stamp()

left(90)

forward(100)

right(60)

forward(70)

shape('square')

color('yellow', 'blue')

stamp()

width(40)

left(45)

forward(90)

stamp()

up()

forward(20)

stamp()

left(90)

forward(100)

end_fill()

down()

width(9)

circle(30)

pencolor(0,200,20)

forward(10)

width(5)

circle(30)

forward(10)

pencolor(0,100,100)

circle(30)

pencolor(100,0,20)

forward(10)

circle(30)

pencolor(200,0,20)

left(20)

forward(20)

circle(20)

pencolor('black')

circle(300)

up()

left(90)

forward(400)

shape('triangle')

shapesize(20)

stamp()




