'''
Created on 2 March 2015
@author: Nesar Ahmed
Pledge:   "I pledge my honor that I have abided by the Stevens Honor System." 

CS115 - Hw 5
'''
import turtle 
import random
# import turtle  # Needed for graphics
# Ignore 'Undefined variable from import' errors in Eclipse.

def svTreeRecursion(trunkLength, levels):
    """Recursive svTree"""
    if levels == 0:
        pass
    else:
        turtle.pencolor(random.choice(["red", "blue", "green", "black", "orange", "brown"]))
        turtle.forward(trunkLength)
        turtle.left(40)
        svTreeRecursion(trunkLength / 2, levels - 1)
        turtle.right(80)
        svTreeRecursion(trunkLength / 2, levels - 1)
        turtle.left(40)
        turtle.backward(trunkLength)

def svTree(trunkLength, levels):
    """Draws a recursive stick tree with a given trunk length and a given number of levels. 
        The tree branches are randomly colored."""
    turtle.speed(10)
    turtle.left(90)
    turtle.pensize(3)
    svTreeRecursion(trunkLength, levels)
    turtle.done()
    
def fastLucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''    
    def fib_helper(n,memo):
        if n in memo:
            return memo[(n)]
        #do work
        if n==0:
            return 2
        elif n==1:
            return 1
        else: 
            result=fib_helper(n-1,memo)+fib_helper(n-2,memo)
        #store and return result
            memo[n]=result
            return result
    return fib_helper(n,{})

# If you did this correctly, the results should be nearly instantaneous.
print(fastLucas(3))  # 4
print(fastLucas(5))  # 11
print(fastLucas(9))  # 76
print(fastLucas(24))  # 103682
print(fastLucas(40))  # 228826127
print(fastLucas(50))  # 28143753123

# Should take a few seconds to draw a tree.
svTree(100, 4)
