'''
Created on Feb 4, 2016

@author: gorav
'''
from cs115 import reduce

def dot(L,K):
    if L ==[] or K ==[]:
        return 0
    return dot(L[1:],K[1:])+L[0]*K[0]
print (dot([5,3],[6,4]))
    

def explode(S):
    if S=='':
        return []
    return [S[0]]+ explode(S[1:])
print (explode('spam'))
   
    
def ind(e,L):
    if L==[] or L=='':
        return 0
    if e==L[0]:
        return 0
    return 1+ind(e,L[1:])
print (ind(2,[1,2,3,4]))


def removeAll(e,L):
    if L==[]:
        return []
    elif e==L[0]:
        return removeAll(e,L[1:])
    return [L[0]]+removeAll(e,L[1:])


def myFilter(e,L):
    if L==[]:
        return []
    if not e(L[0]):
        return myFilter(e,L[1:])
    return [L[0]]+myFilter(e,L[1:])
print (myFilter(lambda x:x==2,[1,2,3,4]))
    

def deepReverse(L):
    if L==[]:
        return []
    elif isinstance(L[0],list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]
    print(deepReverse([1, [2, 3], 4]))