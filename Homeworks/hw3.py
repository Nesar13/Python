'''
Created on: 2/17/16
@author:   Nesar Ahmed
Pledge:   "I pledge my honor that I have abided by the Stevens Honor System."
CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def determine(x, y):
    """Added function for 'giveChange()' that determines 
    which iteration of use_it and lose_it we should return."""
    if 'halt' in x:
        return y
    elif 'halt' in y:
        return x
    elif len(x) >= len(y):
        return y
    return x

def giveChange(amount, coins):
    '''returns minimum number of coins needed to make the amount with the given coins'''
    if amount <= 0:    
        return []
    elif coins == []: 
        return ['halt']
    elif coins[0] > amount: 
        return giveChange(amount, coins[1:])
    else:
        use_it = [coins[0]] + giveChange(amount - coins[0], coins)
        lose_it = giveChange(amount, coins[1:])
        return determine(use_it, lose_it)

print ('Give change:', giveChange(48, [1,5,10,25,50]))
    

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def letterScore(letter, scorelist):
    """Returns the score for a given letter, according to a given score list."""
    if scorelist[0][0] == letter:                #cycles through scorelist to find
        return scorelist[0][1]                    #requested letter, 
    return letterScore(letter, scorelist[1:])     #then returns associated score

def wordScore(S, scorelist):
    """Returns the total score for a word according to a given score list."""
    if S == '':
        return 0                        
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist) 


def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(scrabbleScores, Dictionary) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []: 
        return []
    return [[dct[0], wordScore(dct[0], scores)]] + wordsWithScore(dct[1:], scores)

print ("Testing wordsWithScore")
print (wordsWithScore(Dictionary,scrabbleScores))

'''use_it +=L[0] -> use_it=use_it+L[0]'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

def take(n, L):
    if n == 0:
        return []
    return [L[0]]+take(n-1,L[1:])

# Code to use for testing
def test_Take(n,L):
    if take(n,L)==L[0:n]:
        print ("test is okay")
    else: print ("my test failed")


test_Take(0, ["not", "it", "works", "!"])
test_Take(2, ["not", "it", "works", "!"])
test_Take(4, ["not", "it", "works", "!"])
    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    if n == 0:
        return L
    return drop(n-1,L[1:])

def test_Drop(n,L):
    if drop(n,L)==L[n:]:
        print ("test ok")
    else: print ("my test failed")

test_Drop(0, ["I", "am", "nearly", "done"])
test_Drop(1, ["I", "am", "nearly", "done"])
test_Drop(3, ["I", "am", "nearly", "done"])



