'''
Created on 4 March 2015
@author:   Nesar Ahmed
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Lab 6
'''
from builtins import str
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

print (isOdd(41))
#42 in decimal is 101001
#An odd decimal number will have binary value of  1 in the rightmost place
#An even will have a 0 in the rightmost binary
#eliminating the LSB will reduce the decimal value by half
#when N is odd, Y will be 1 for its base, N is even, Y is 0
def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n==0:
        return ''
    binary= ''
    tmp=n//2
    if tmp> 0:
        binary +=numToBinary(tmp)
        binary += str(n % 2)
    else:
        binary=str(n % 2)
    return binary

print (numToBinary(8))


def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s=='':
        return 0
    return binaryToNum(s[:-1])*2+int(s[-1])
    
print (binaryToNum('1000'))

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    a=numToBinary(binaryToNum(s) + 1)
    if len(a) < len(s):
        a=str(0)*(len(s)-len(a)) + a
    return a
    
    
print (increment('00000111'))

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n == 0:
        print(s)
    else:
        print(s)  
        count(increment(s), n-1)


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    if n % 3 == 0:
        return numToTernary(n//3) + str(0)
    if n % 3 == 1:
        return numToTernary(n//3) + str(1)
    return numToTernary(n//3) + str(2)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    return ternaryToNum(s[:-1])*3 + int(s[-1])