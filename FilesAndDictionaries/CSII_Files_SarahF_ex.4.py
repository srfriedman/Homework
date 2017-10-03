#HTCS 11.8 Exercise 1
#Sarah Friedman
#9/13/17

import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-400, -400, 400, 400)

file = open("labdata.txt")

def plotRegression(file):
    for line in file:
        index = line.split()
        xcoord = index[0]
        xcoord = xcoord.replace('[', '')
        xcoord = xcoord.replace(']', '')
        xcoord = int(str(xcoord))

        ycoord = index[1]
        ycoord = ycoord.replace('[', '')
        ycoord = ycoord.replace(']', '')
        ycoord = int(str(ycoord))

        #print(index, xcoord)

        t.penup()
        t.goto(xcoord, ycoord)
        t.pendown
        t.dot(3)
        t.penup()

        t.goto(0, 0)


t.forward(300)
t.back(300)
t.right(90)
t.forward(300)
t.back(300)
t.right(90)
t.forward(300)
t.back(300)
t.right(90)
t.forward(300)
t.back(300)

plotRegression(file)

wn.exitonclick()
