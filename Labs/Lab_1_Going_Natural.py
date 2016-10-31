'''
Created on Jan 28, 2016

@author: nahmed3
'''
import math
from cs115 import map, reduce 

n=float(input('Enter a number: '))

def inverse(n):
    return 1/n 
print  ('The inverse is: ', inverse(n))


def add(x,y):
    return x+y

n=abs(int(input('Enter another number for Taylor expansion: ')))
def e(n):
    return reduce(add,(map(inverse, map(math.factorial,(range(0,n+1))))))
print ('The Taylor expansion is:', e(n))

def error(n):
    return abs(math.e-e(n))
print ('The error is:', error(n))
def error_percentage(n): 
    return (abs(((math.e- e(n))/math.e)) *100)
print ('The percent error is:', error_percentage(n),'%')
    

