''' "I pledge my honor that I have abided by the Stevens Honor System." 


@author: Nesar Ahmed
Created on Feb 24, 2016
'''

def pascal_row(n):
    """The pascal function returns the nth row of pascal's triangle,
        where the 0th row is [1] """
    if n < 0:
        return float("inf")
    if n == 0:
        return [1]
    return next_row(pascal_row(n-1))    
    
def next_row(previous_row):
    """Takes a row from the pascal triangle and returns the next row"""
    def next_row(previous_row):
        if [previous_row[0]] == previous_row:    
            return [1]
        answer = [previous_row[0] + previous_row[1]] + next_row(previous_row[1:])
        return answer
    return [1] + next_row(previous_row)
    
def pascal_triangle(n):
    '''takes a single input ant returns a list of lists
        of pascal's triangle up to and including n'''
    if n < 0: 
        return float("inf")
    if n==0:
        return [[1]]
    return pascal_triangle(n-1)+[pascal_row(n)]
        


    