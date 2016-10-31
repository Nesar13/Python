#
# life.py - Game of Life lab
#
# Name:Nesar Ahmed
# Pledge:I pledge my honor that I have abided by the Stevens Honor System
#

import random, sys
from _hashlib import new

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row
print (createOneRow(5))


def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] 
    return A
print (createBoard(4, 6))

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
print(printBoard([1,2,3]))

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A        


def innerCells(w,h):
    ''' returns a 2d array of all live cells - with the value of 1 - except for
    a one-cell-wide border of empty cells (with the value of 0) around the edge 
    of the 2d array.'''
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or row == (h-1) or col == 0 or col == (w-1):
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A 
    


def randomCells(w,h):
    ''' returns an array of randomly-assigned 1's and 0's except that the outer 
    edge of the array is still completely empty (all 0's) as in the case of 
    innerCells.'''
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if row == 0 or row == (h-1) or col == 0 or col == (w-1):
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A 


def copy(A):
    '''make a deep copy of the 2d array A. Thus, copy will take in a 2d array A 
    and it will output a new 2d array of data that has the same pattern as the 
    input array.'''
    new = createBoard(len(A), len(A[0]))
    for row in range(len(A[0])):
        for col in range(len(A)):
            new[row][col] = A[row][col]
    return new    
    
def innerReverse(A):
    ''' takes an old 2d array (or "generation") and then creates a new generation 
    of the same shape and size (either with copy, above, or createBoard).'''
    B = copy(A)
    for row in range(1, len(A)-1):
        for col in range(1, len(A[0])-1):
            if A[row][col] == 1:
                return 0
            else:
                B[row][col] == 1
    return B


def countNeighbors( row, col, A ):
    count = 0
    for x in range(col-1, col+2):
        for y in range(row-1, row+2):
            if A[y][x] == 1:
                count += 1
    if A[row][col] == 1:
        return count - 1
    return count
A = [ [0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
#printBoard(A)

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0."""
    X = copy(A)
    h = len(A)
    w = len(A[0])
    for row in range(1, h-1):
        for col in range(1, w-1):
            count = countNeighbors(row, col, A)
            if count < 2:
                X[row][col] = 0
            if count > 3:
                X[row][col] = 0
            if A[row][col] == 0 and count == 3:
                X[row][col] = 1
    return X
#A2 = next_life_generation( A )
#printBoard(A2)
    