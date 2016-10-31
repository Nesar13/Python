'''
Created on March 3, 2016
@author: Chelsea Aure
Pledge: I pledge my honor that I have abided by the Stevens Honor System. -C.A.

CS115 - Homework 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5


# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code. 

#helper functions for def compress(S)
#these need to be BEFORE the function itself (didn't work when put before the compress function)
def numToBinary(k, n): # we learned this helper function in lab
    '''This helper function returns the string with the binary representation of non-negative integer n.     
    If n is 0, the empty string is returned.'''     
    def binary(n):
        if n==0:
            return ''
        elif n%2==1:
            return binary(n//2)+'1'
        else:
            return binary(n//2)+'0'
    R = binary(n) #this part is so that we can format to k bytes
    if len(R) <= k:
        answer= '0' * (k-len(R)) + R
    elif len(R)>k:
        answer= R[-k:]
    return answer

def count_zero(s):
    '''This helper function counts the amount of consecutive zeros at the beginning of a string'''
    if s=="":
        return 0
    elif s[0]=='1':
        return 0
    else:
        return 1 + count_zero(s[1:])

def count_one(s):
    '''This helper function counts the amount of  number of consecutive ones at the beginning of a string.'''
    if s=="":
        return 0
    elif s[0]=='0':
        return 0
    else:
        return 1 + count_one(s[1:])  
#end helper functions for compress

def compress(S):
    '''Compress should take a binary string length of 64 and returns another binary string as output'''
    def compress_helper(s, memo):
        if s=="":
            return ""#if there is an empty string, return empty string
        elif s[0]=='\n':#i didn't understand this line
            return compress_helper(s[1:])#but whatever it means, it says to send the next letter of the string
        elif memo==0:
            countzero = count_zero(s)#this will count the amount of consecutive zeros in your binary string
            countzero = min(MAX_RUN_LENGTH, countzero) #this returns the smaller one (either the counted zeros or the number of bits for data in the original format aka 16)
            return str(numToBinary(COMPRESSED_BLOCK_SIZE, countzero))+ compress_helper(s[countzero:],1)
        elif memo==1:#essentially this repeats what is above, but memo==1 this time
            countone= count_one(s)
            countone= min(MAX_RUN_LENGTH, countone)
            return str(numToBinary(COMPRESSED_BLOCK_SIZE, countone))+ compress_helper(s[countone:],0)
        else:
            pass
    return compress_helper(S, 0)

#compress can sometimes give output that is actually longer than the input, the largest number of bits depends on the number of different colors that you choose
#say if you chose the primary colors in the color wheel (red, blue, yellow) in your 64 bit image, then you'd have a 64 bit input but a longer output of 3*64 output because of the colors
         
def uncompress(C):
    '''Uncompress undoes the compressing done in compress'''
    def uncompress_helper(u, memo):
        if u=='':
            return''
        elif memo==0:
            return int(u[0:COMPRESSED_BLOCK_SIZE],2)*'0'+uncompress_helper(u[COMPRESSED_BLOCK_SIZE:], 1)
        else:
            return int(u[0:COMPRESSED_BLOCK_SIZE],2)*'1'+uncompress_helper(u[COMPRESSED_BLOCK_SIZE:], 0)
    return uncompress_helper(C, 0)

def compression(S):
    '''Compression returns the ratio of the compressed size to the original size for image s'''
    original_size = len(S)
    new_image = compress(S)
    new_size = len(new_image)
    ratio = float((new_size)/(original_size))
    return ratio

Penguin = '00011000'+'00111100'*3 + '01111110'+'11111111'+'00111100'+'00100100'
Smile = '0'*8 + '01100110'*2 +'0'*8 +'00001000' + '01000010' + '01111110' + '0'*8
Five =   '1'*9 + '0'*7 + '10000000'*2 + '1'*7 + '0' + '00000001'*2 + '1'*7 + '0' 
StripedBeachBlanket ='01010101'*8
ChristmasTree = '00011000'+'00111100'*3 + '01111110'+'11111111'+'00111100'+'00011000'
UpSign = '00011000'+'00111100'+ '01111110'+ '00011000'*4
#I added The striped beach blanket, the christmas tree, and the upsign
#It's best to draw these out on an 8x8 square and choosing your 1's and your 0's

testing_Images = [Penguin, Smile, Five, StripedBeachBlanket, ChristmasTree, UpSign]  

def test():
    for i in testing_Images:
        curtail=compress(i)
        elongate=uncompress(curtail)
        if i!= elongate:
            print ("error") 
        else:
            print ("pass")
        print (compression(i))

if __name__ == '__main__':
    test()
    
#Lai’s algorithm would only work if his algorithm tested other algorithms, then returned the most-curtailed string. His uncompress function does not backtrack to know the used algorithm, so his functions do not work. Yes. He is LAI-ing.