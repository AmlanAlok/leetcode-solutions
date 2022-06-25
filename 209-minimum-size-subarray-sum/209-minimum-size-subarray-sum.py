'''
7
[2,3,1,2,4,3]
4
[1,4,4]
11
[1,1,1,1,1,1,1,1]
11
[1,2,3,4,5]
'''
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return ans1(target, nums)
    
'''
Two Pointer/ Sliding Window
TC = n
SC = 1
'''
def ans1(target: int, nums: List[int]) -> int:
    
    m = sys.maxsize
    i, j = 0, 0
    l = len(nums)
    s = 0
    
    while j < l:
        
        while s < target and j < l:
            s+=nums[j]
            j+=1
        
        while s >= target and i < l:
            if m > (j-i):
                m = j-i
            s-=nums[i]
            i+=1
        
    return 0 if m == sys.maxsize else m
        
            
        
        
        
        
            
        
    
    
    
    
    