'''
Created on:9 March 2016
@author:   Nesar Ahmed
Pledge:    "I pledge my honor that I have abided by the Stevens Honor System."
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.


def compress(S):
    """Takes binary string S of length 64 and returns another binary string as output. 
        The output will be a run-length encoding of the input string."""
    
    def recurse(T, memo):
        if T == "":
            return ""
        elif T[0] == '\n':
            return recurse(T[1:])
        elif memo == 0:
            zerocount = zero_count(T)
            zerocount = min(MAX_RUN_LENGTH, zerocount)
            return str(numToBinary(COMPRESSED_BLOCK_SIZE, zerocount)) + recurse(T[zerocount:],1) #GLOBAL COMPRESSED_BLOCK_SIZE
        elif memo == 1:
            onecount = one_count(T)
            onecount = min(MAX_RUN_LENGTH, onecount)
            return str(numToBinary(COMPRESSED_BLOCK_SIZE, onecount)) + recurse(T[onecount:],0) #GLOBAL 
        else:
            pass

    return recurse(S, 0)

 
 

        # I use numToBinary() instead of the built in bin() to avoid the '0b' 
        # that leads output from bin(), and also to format the string to 
        # k bytes
        
# If the colors alternated fast enough, your output string would be longer than the
# input string. For example, if you used 5 bits to represent each run of colors, and 
# the input was a checkerboard, you would end up with 5*64 bits of output, much longer
# than the 64 bits of output. 
        
##compress helper functions##
    
def zero_count(S):
    """Counts the number of consecutive zeros at the beginning of a binary string."""
    if S == '':
        return 0
    elif S[0] == '1':
        return 0
    else:
        return 1 + zero_count(S[1:])
        
def one_count(S):
    """Counts the number of consecutive ones at the beginning of a binary string."""
    if S == '':
        return 0
    elif S[0] == '0':
        return 0
    else:
        return 1 + one_count(S[1:])

def numToBinary(k, n):
    ''' converts number to binary number bit size k'''
    def binary(n):
        if n == 0:
            return ''
        elif n%2 == 1:
            return  binary(n//2)+'1'
        else:
            return binary(n//2)+ '0'
    temp = binary(n)
    if len(temp) <= k:
        answer = '0' * (k - len(temp)) + temp
    elif len(temp) > k:
        answer = temp[-k:]
    return answer

        
##end of helper functions##
                
def uncompress(C):
    """Takes a run-length encoded string as input and returns the original string."""
    def uc(C, memo):
        if C == '':
            return ''
        elif memo == 0:
            return int(C[:COMPRESSED_BLOCK_SIZE],2) * '0' + uc(C[COMPRESSED_BLOCK_SIZE:], 1) #GLOBAL 
        else:
            return int(C[:COMPRESSED_BLOCK_SIZE],2) * '1' + uc(C[COMPRESSED_BLOCK_SIZE:], 0) #GLOBAL COMPRESSED_BLOCK_SIZE
    return uc(C, 0)
        
def compression(S):
    """Returns the ratio of the sizes of the compressed and uncompressed versions of S."""
    originalsize = len(S)
    newimage = compress(S)
    newsize = len(newimage)
    ratio = float(newsize)/float(originalsize)
    return ratio

 


Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
Smile = "0"*8 + "01100110"*2 +"0"*8 +"00001000" + "01000010" + "01111110" + "0"*8
Five =   "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0" 
Bars = "0" * 16 + "1" * 16 + "0" * 16 + "1" * 16
onesAndZeros = [i % 2 for i in range(1,65)]
Checker = ''.join(map(str,onesAndZeros))
Zeros = '0' * 64

testImages = [Penguin, Smile, Five, Bars, Checker, Zeros]

def test():
    for i in testImages:
        short = compress(i)
        unshort = uncompress(short)
        if i != unshort:
            print ("error") 
        else:
            print ("pass")
        print (compression(i))

if __name__ == '__main__':
    test()



# The only way Lai's algorithm would always shorten the string would be if the algorithm 
# tried several different algorithms, then returned the one that shortened the string 
# the most.  Then, to uncompress the algorithm, the uncompression function would not
# know which algorithm was used. 