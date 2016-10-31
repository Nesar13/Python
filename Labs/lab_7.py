# If the integer is odd, the right-most bit would be 1. If the integer is even, the right-most bit would be 0
# from 1010 to 1011, the value of the number is changing in that the last recursive call to the number is not divisible by 2.

s = '00000000'
def isOdd(n):
    if n == 0:
        return False
    elif n % 2 == 0:
        return False
    else:
        return True

def numtoBinary(n):
    if n == 0:
        return ''
    elif isOdd(n):
        return numtoBinary(n/2) + '1'
    else:
        return numtoBinary(n/2) + '0'
def Binarytonum(s):
    if s == '':
        return 0
    else:
        return int(s[-1]) + 2 * Binarytonum(s[:-1])
def increment(S):
    num = Binarytonum(S) + 1
    plusone = numtoBinary(num)
    if len(S) == 8:
        return S
    else:
        return plusone
def count(S,n):
    if n == 0:
        return S
    elif n !=0:
        print (increment(S))
    else:
        return count(S,n-1)
        
