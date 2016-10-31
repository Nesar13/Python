''' "I pledge my honor that I have abided by the Stevens Honor System." 


@author: Nesar Ahmed
Created on Mar 26, 2016
'''
def isOdd(n):
    '''a complementary function, checks if a number is odd'''
    if n == 0:
        return False
    elif n % 2 == 0:
        return False
    return True

def numtoBinary(n):
    '''converts a number to binary'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numtoBinary(n//2) + '1'
    else:
        return numtoBinary(n//2) + '0'
print (numtoBinary(32))
def Binarytonum(s):
    '''converts a binary number to decimal'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + 2 * Binarytonum(s[:-1])
def TcToNum(s):
    '''converts 2's complement number to decimal value'''
    if s == "":
        return 0
    elif len(s) > 8:
        return ""
    elif len(s) < 8:
        return ""
    elif Binarytonum(s) >= 128:
        Negnum = (255 - Binarytonum(s) + 1)*-1
        return Negnum
    else:
        return Binarytonum(s)
    
def NumToTc(n):
    '''converts number to 2's complement'''
    if n >=128 or n <= -129:
        return 'Error'
    if n==0: 
        return '00000000'
    elif n < 0:
        N = n*-1
        negBin = numtoBinary(255-(N-1))
        B = 8-len(negBin)
        return B*'0' + negBin
    elif n > 0 and n < 128:
        bin1 = numtoBinary(n)
        C = 8-len(bin1)
        return C*'0' + bin1

