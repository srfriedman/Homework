#HTCS 11.8 Exercise 1
#Sarah Friedman
#9/13/17

file = open("mystery.txt", "r")

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-400, -400, 400, 400)


for line in file:
    index = line.split()
    if index[0] == "UP":
        t.penup()
    else:
        if index[0] == "DOWN":
            t.pendown()
        else:
            t.goto(int(index[0]), int(index[1]))

