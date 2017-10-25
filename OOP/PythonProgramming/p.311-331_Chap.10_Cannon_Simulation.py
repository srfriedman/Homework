#Reading p. 297-311
#10/16/17
#Sarah Friedman

#Projectile Exercise

from projectile import *

height = []

def getInputs():
    a = eval(input("Enter the launch angle (in degrees): "))
    v = eval(input("Enter the initial velocity (in meters/sec): "))
    h = eval(input("Enter the initial height (in meters): "))
    t = eval(input("Enter the time interval between position calculations: "))

    return a, v, h, t


def main():
    angle, vel, h0, time = getInputs()
    cball = Projectile(angle, vel, h0)
    while cball.getY() >= 0:
        cball.update(time, height)
    print("\nDistance traveled: {0:0.1f} meters".format(cball.getX()))
    print("Max height: ", max(height))

main()
