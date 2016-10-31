'''
Created on Jan 30, 2016

"I pledge my honor that I have abided by the Stevens Honor System." 

@author: nahmed3 (Nesar Ahmed)
'''
from cs115 import reduce, map

#This will define a factorial
def mult(x,y):
    return x*y
n=abs(int(input("Enter an integer to find factorial: ")))
      
def factorial(n):
    return reduce(mult, range(1,n+1)) #reduces iterable to a single value

print (n,'! =', factorial(n))
#end 
#This will find the average from a list of inputs 
def add(x,y):
    return x+y 

lst=(input('Enter a list of numbers separated by spaces: '))
L=map(int, lst.split())

def mean(L):
    return float((reduce(add,L ))/(len(L))) #len() returns the amount of numbers in a list

print ('mean =', mean(L))
#end 
#Testing for prime numbers
 
n= abs(int(input('Enter another number to check for prime: ')))

def divides(n):
    def div(k):
        return n % k==0
    return div

def primes(n):
    if n == 2: return True
    lst = map(divides(n), range(2, n)) #checks to see if n/krange is either false or true
    return sum(lst) == 0 #sum of primes #'s add up to 0 with boolean logic

print ('Is this a prime number?:',  primes(n))