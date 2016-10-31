'''
Created on Feb 5, 2016

@author: nahmed3
'''
def length(lst):
    if lst==[]:  
        return 0
    return 1+length(lst[1:])

def dot(L,K): 
    '''takes the dot product of a list'''
    if L==[] or K==[]:
        return 0
    return dot(L[1:], K[1:]) + L[0]*K[0]

print (dot ([1,2,3], [1,2,3]))
           
           
def explode(S):
    '''eg explode('spam') => ['s', 'p', 'a' , 'm']'''
    if S=='':
        return []
    return [S[0]] + explode(S[1:])

print (explode('spam')) 

def ind(e,L):
    '''takes an element e and returns the first location of it in L'''
    if L==[] or L=='':
        return 0
    if e==L[0]:
        return 0
    return 1+ind(e,L[1:])

print ("ind:", (ind(2, [1,3,2,4])))


def removeAll(e, L):
    '''removes the same e value from a list L'''
    if L==[]: 
        return []
    elif e==L[0]:
        return removeAll(e,L[1:])
    return [L[0]]+removeAll(e,L[1:])

print (removeAll(5,[1,2,3,4,5])) 

def myFilter(e,L):
    '''makes a filter function'''
    if L==[]:
        return []
    if not e(L[0]):
        return myFilter(e,L[1:])
    return [L[0]]+myFilter(e,L[1:])
print (myFilter(lambda x:x%2==0,[1,2,3,4]))

def deepReverse(L):
    '''deepReverse reverses the list, even if there's another list inside'''
    if L==[]: 
        return []
    elif isinstance(L[0],list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else: 
        return deepReverse(L[1:]) +[L[0]]
         
print (deepReverse([1, [2,3],4]))


            
           
           
    
