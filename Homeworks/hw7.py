''' "I pledge my honor that I have abided by the Stevens Honor System." 


@author: Nesar Ahmed
Created on Mar 14, 2016
'''

def numToBaseB(N, B):
    """converts base 10 number to base B"""
    if N == 0:
        return ""
    else:
        return numToBaseB(N//B, B) + str(N%B)
#print (numToBaseB(4, 3))    
   
def baseBToNum(S, B):
    """converts base B number to base 10"""
    if S == "":
        return 0
    else:
        return int(S[0])*(B**(len(S)-1))+baseBToNum(S[1:], B)

#print (baseBToNum ("11",2))      
       
def baseToBase(B1,B2,SinB1):
    """converts number of base B1 to number of base B2"""
    number = baseBToNum(SinB1, B1)
    return numToBaseB(number, B2)
#print (baseToBase(2,10,'11'))
    
def add(S, T):
    """adds two binary strings by converting them to decimal, 
        adding, then converting back to binary"""
    num1 = baseBToNum(S, 2)
    num2 = baseBToNum(T, 2)
    sum_ = num1 + num2
    return numToBaseB(sum_, 2)

#print (add("11", "01"))
    

FullAdder = { 
#Each row has (x,y,carry-in) : (sum_, carry-out)
('0','0','0') : ('0','0'),
('0','0','1') : ('1','0'),
('0','1','0') : ('1','0'),
('0','1','1') : ('0','1'),
('1','0','0') : ('1','0'),
('1','0','1') : ('0','1'),
('1','1','0') : ('0','1'),
('1','1','1') : ('1','1') }
        
        
def addB(S, T):
    """Adds two binary strings using the full adder algorithm"""
    def add(S, T, C):
        """implementation of full adder algorithm for addB"""
        if S == "" and T == "" and C == "0":
            return ""
        
        elif S == "" and T == "" and C == "1":
            return "1"
        
        elif S == "":
            x = '0'
            y = T[-1]
            c = C[0]
            tup = FullAdder[(x,y,c)]
            sum_ = tup[0]
            co = tup[1]
            sum_, co = FullAdder[(x,y,c)]
            return add(S, T[:-1], co) + sum_
        
        elif T == "":
            x = S[-1]
            y = '0'
            c = C[0]
            sum_, co = FullAdder[(x,y,c)]
            return add(S[:-1], T, co) + sum_
    
        x = S[-1]
        y = T[-1]
        c = C[0]
        sum_, co = FullAdder[(x,y,c)]
        return add(S[:-1], T[:-1], co) + sum_
        
    return add(S, T, '0')

        



    
