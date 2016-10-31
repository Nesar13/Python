# mandelbrot.py
# Lab 9
# "I pledge my honor that I have abided by the Stevens Honor System."
# Name:Nesar Ahmed

# keep this import line...
from cs5png import *
import turtle

# start your Lab 8 functions here:
def mult( c, n ):
    """ mult uses only a loop and addition 
    to multiply c by the integer n"""
    result = 0
    for x in range( n ):
        result+= c
    return result

print (mult(3, 9))

def update(c,n):
    '''update starts with z=0 and runs 
    z=z**2 + c for a total of n times. It returns
    the final z'''
    z=0
    for x in range(n):
        z=z**2+c
    return z
print(update(-1, 10))

def inMSet(c,n):
    '''inMSet takes in c for the update step of z=z**2+c
    n, the maximum number of times to run that step.
    Then, it should return False as soon as abs(z) gets 
    larger than 2; Trues if abs(z) never gets larger than 2
    (for n iterations)'''
    z=0+0j
    for x in range(n):
        z=z**2+c
        if abs(z)>2:
            return False
    return True

#c=0.42+0.2j
#print(inMSet(c, 25))

def scale(pix,pixMax,floatMin,floatMax):
    """ scale takes in pix, the CURRENT pixel column (or row)
     pixMax, the total # of pixel columns floatMin, the min floating-point 
     value floatMax, the max floating-point value scale returns the 
     floating-point value that corresponds to pix"""
    return ((pix/pixMax)*(floatMax-floatMin))+floatMin
print(scale(100, 200, -2.0, 1.0))

def mset():
    width=300
    height=200
    turtle.speed(0)
    turtle.tracer(0,0)
    turtle.screensize(width,height)
    turtle.setworldcoordinates(0,0,width,height)
    turtle.setpos(0,0)
    turtle.penup()
    image=PNGImage(width,height)
    for col in range(width):
        for row in range(height):
            turtle.setpos(col,row)
            #CODE HERE
            x= scale(col,width,-2,1)
            y=scale(row,height,-1,1)
            c=x+y*1j
            if inMSet(c,25):
                turtle.dot()
    turtle.update()
    turtle.done()
print(mult(3,4))
print(update(-1,3))
c = 3+4*1j
print(inMSet(c,25))
print(scale(100,300,-2,1))

mset()
    