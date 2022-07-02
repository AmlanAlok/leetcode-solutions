'''
[[1,3],[2,2],[3,1]]
4
[[5,10],[2,5],[4,7],[3,9]]
10
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        return ans1(boxTypes, truckSize)

'''
Sorted Array
TC = n log n 
SC = 1
'''
def ans1(numsList, t):
    
    l = len(numsList)
    
    # O(n log n)
    # numsList = sorted(numsList, key= lambda nums: nums[1], reverse = True)
    numsList.sort(key= lambda nums: nums[1], reverse = True)
    
    row = 0
    xsum = 0
    
    while t > 0 and row < l:
        
        if numsList[row][0] > 0:
            numsList[row][0] -= 1
            xsum += numsList[row][1]
            t -= 1
        if numsList[row][0] == 0:
            row += 1
            
    return xsum
            

''' Recursion - Not working rn'''    
def ans4(numsList, t):
    return (recur(numsList, t, 0))
                
    
def recur(numsList, t, xsum):

    if t == 0:
        return xsum
    
    p = []
    
    for row in range(len(numsList)):
        if numsList[row][0] > 0:
            
            numsList[row][0] -= 1
            xsum += numsList[row][1]
            t -= 1
            
            x = recur(numsList, t, xsum)
            if x:
                p.append(x)
    
    if p:
        return max(p)
    
        
        