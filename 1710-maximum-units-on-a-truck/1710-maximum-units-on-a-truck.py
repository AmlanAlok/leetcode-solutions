'''
[[1,3],[2,2],[3,1]]
4
[[5,10],[2,5],[4,7],[3,9]]
10
[[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
35
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
        
        x, y = numsList[row][0], numsList[row][1]
        
        if x > 0:
            if x <= t:      # I did not add this to speed up the logic earlier
                numsList[row][0] = 0
                xsum += x*y
                t -= x
            else:
                numsList[row][0] -= 1
                xsum += y
                t -= 1
        if x == 0:
            row += 1
            
    return xsum

def ans2(boxTypes: List[List[int]], truckSize: int):
    boxTypes.sort(key = lambda x: x[1],reverse=True)
    n = len(boxTypes)
    final = 0
    for i in range(n):
        boxes, units= boxTypes[i]
        if truckSize >= boxes:
            truckSize -= boxes
            final += boxes*units
        elif truckSize < boxes:
            while truckSize > 0 and boxes > 0:
                truckSize -= 1
                boxes -= 1
                final += units
    return final
            

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
    
        
        