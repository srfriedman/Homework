#Letter Count Histogram
#Sarah Friedman
#9/18/17

import turtle
t = turtle.Turtle()
t2 = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(-400, -400, 400, 400)

string = str(input("Input a string: "))

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

letterVal = []

dictionary = {}

def drawChart(t, tt):
    tt.ht()

    t.penup()
    t.backward(300)
    t.right(90)
    t.backward(300)
    t.pendown()
    t.forward(600)
    t.left(90)

    tt.penup()
    tt.goto(-300, -315)

    x = 0

    t.forward(11.5)
    tt.forward(11.5)
    t.dot(5)
    tt.write(alphabet[x])
    x = x+1
    for letter in range(25):
        t.forward(23)
        tt.forward(23)
        t.dot(5)
        tt.write(alphabet[x])
        x = x+1
    t.ht()


def countAll(text):
    for letter in text:
        dictionary[letter] = text.count(letter)


def countAppearance():
    global dictionary, alphabet
    x = 0

    for l in range(26):
        letter = alphabet[x]
        if letter in dictionary:
            letterVal.append(dictionary[letter])
            x = x+1
        else:
            letterVal.append(0)
            x = x+1
    return letterVal


countAll(string)
print("Dict: ", dictionary)

def draw(val, t):
    x = 0
    t.penup()
    t.goto(-300, -300)
    t.pendown()

    for x in val:
        if x > 0:
            t.forward(11.5)
            t.left(90)
            t.forward((x)*15)
            t.write(x)
            t.right(90)
            t.forward(11.5)
            t.right(90)
            t.forward((x)*15)
            t.left(90)
            x = x+1
        else:
            t.forward(23)
            x = x+1
    t.ht()



countAll(string)
countAppearance()
print(letterVal)

drawChart(t, t2)
draw(letterVal, turtle)

wn.exitonclick()
