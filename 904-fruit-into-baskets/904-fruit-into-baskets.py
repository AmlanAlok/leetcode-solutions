'''
[1,2,1]
[0,1,2,2]
[1,2,3,2,2]
[3,3,3,1,2,1,1,2,3,3,4]
'''

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        return ans1(fruits)
    
def ans1(nums: List[int]) -> int:
    
    d = {}
    i=j=0
    m=0
    l = len(nums)
    
    while j<l:
        
        while j<l and len(d.items()) <= 2:
            n = nums[j]
            
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            
            mlen = (j-i+1)
            
            if m < mlen and len(d.items()) <= 2:
                m = mlen
                
            j+=1
        
        while i<l and len(d.items()) > 2:
            
            n = nums[i]
            
            d[n]-=1
            
            if d[n] == 0:
                del d[n]
                
            i+=1
    
    return m
            
            
            
    