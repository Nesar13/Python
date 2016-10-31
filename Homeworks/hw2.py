'''
Created on ___2/10/16____________________
@author:   Nesar Ahmed_______________________
Pledge:  "I pledge my honor that I have abided by the Stevens Honor System."

CS115 - Hw 2
'''
import sys
from cs115 import filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo','spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    """Returns the score for a given letter, according to a given score list."""
    if letter=='':
        return ''
    if scorelist[0][0] == letter:                #cycles through scorelist to find
        return scorelist[0][1]                    #requested letter, 
    return letterScore(letter, scorelist[1:])     #then returns associated score

print (letterScore('z', scrabbleScores))

def wordScore(S, scorelist):
    """Returns the total score for a word according to a given score list."""
    if S == '':
        return 0                        
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist) 
#print (wordScore('spam', scrabbleScores))   
    
def wordinrack(rack, word):
    """returns True if word can be obtained from a list of strings"""
    lst_ = rack[:]
    for c in word:
        if c in lst_:
            lst_.remove(c)
        else:
            return False
    return True                  
#print (wordinrack(["a", "s", "n", "f", "o"], "soon"))                 #If a letter is not in the rack, return False
#print (wordinrack(["a", "s", "n", "f", "o"], "asn"))

def ind(e, L):
    """returns the index where e is first found in L"""
    if L[0] == e:
        return 0                        #counts up number of cycles it 
    return 1 + ind(e,L[1:])             #takes to find requested item

def scoreList(rack):
    """Takes a rack of letters as input and returns the 
    different words you could play and their corresponding scores."""    
    possiblewords = filter(lambda x: wordinrack(rack, x), Dictionary)     #creates list of possible words
    def output(lst):
        if lst == []:                                                    #Function that formats output
            return []
        return [[lst[0], wordScore(lst[0],scrabbleScores)]] + output(lst[1:])     
    return output(possiblewords)
print (scoreList(["a","s","m","t","p","o","f"]))


'''def bestWord(rack):
    """Takes a rack of letters and returns the best word you could play and its score"""
    if rack=='': 
        return ''
    possiblewords = filter(lambda x: wordinrack(rack, x), Dictionary)     #creates a list of possible words from rack
    scores = map(lambda x: wordScore(x, scrabbleScores), possiblewords)    #creates corresponding list of scores
    return [possiblewords[ind(max(scores),scores)],max(scores)]            #uses index and max functions to 
                                                                        #return biggest word and its score
#print (bestWord(['g', 'y', 'e']), ['', 0])'''

def bestWord(Rack):
    def better_word(x,y):
        if x[1]> y[1]: 
            return x
        return y 


