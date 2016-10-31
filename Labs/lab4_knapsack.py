'''
Created on Feb 18, 2016
"I pledge my honor that I have abided by the Stevens Honors System."

@author: nahmed3(Nesar Ahmed
'''


    

def knapsack(capacity, itemList): 
    '''returns the maximum item value with a given capacity'''
    if capacity ==0 or itemList==[]:
        return [0,[]]
    elif capacity < itemList[0][0]:
        return knapsack(capacity,itemList[1:])
   
    lose_it=knapsack(capacity,itemList[1:])
    use_it=knapsack(capacity-itemList[0][0],itemList[1:])
    use_it[0]=itemList[0][1]+use_it[0]
    use_it[1]=[itemList[0]]+use_it[1]
    if use_it[0]>lose_it[0]:
        return use_it
    return lose_it
    
print (knapsack(6, [[1, 4], [5, 150], [4, 180]]))
#score =map(lambda x: x+itemList[0][1], use_it) 





















