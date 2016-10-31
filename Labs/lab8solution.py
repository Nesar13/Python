s = "10000000"

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
def TcToNum(s):
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
    if n < 0:
        N = n*-1
        negBin = numtoBinary(255-(N-1))
        B = 8-len(negBin)
        return B*'0' + negBin
    elif n > 0 and n < 128:
        bin1 = numtoBinary(n)
        C = 8-len(bin1)
        return C*'0' + bin1
    elif n >=128:
        return 'Error'
   
