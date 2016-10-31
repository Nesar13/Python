'''
Created on Feb 12, 2016
"I pledge my honor that I have abided by the Stevens Honor System"
@author: nahmed3 (Nesar Ahmed)
'''
def subset_with_values(target, lst):
    #gets the possible numbers that add up to the target
    if target ==0: 
        return [True,[]]
    if lst ==[]: 
        return [False,[]]
    use_it=subset_with_values(target - lst[0],lst[1:])
    if use_it[0]:
        return [True, use_it[1]+[lst[0]]]
    return subset_with_values(target, lst[:1])

#print (subset_with_values(58, [25,10,5,1]))

def change (amount,coins):
    '''returns the minimum number of coins required to make the target amount'''
    if amount==0:
        return 0
    if coins==[]:
        return float("inf")   
    if coins[0]>amount:
        return change(amount, coins[1:])
    use_it=change(amount-coins[0],coins)+1
    lose_it=change(amount,coins[1:])
    return min(use_it,lose_it)
    



print(change(50, [1, 5, 10, 20, 50, 100]))
    
    

    
        