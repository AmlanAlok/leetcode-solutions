'''
[100,4,200,1,3,2]
[0,3,7,2,5,8,4,6,0,1]
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return ans1(nums)
    
def ans1(nums):
    
    n = len(nums)
    
    d = {v:i for i, v in enumerate(nums)}
    
    # print(d)
    
    xmax = 0
    # l = 0
    
    for i in range(n):
        
        v = nums[i]
        
        if v-1 not in d:
            x = v
            l = 0
            while x in d:
                l+=1
                x+=1
            
            xmax = max(xmax, l)
    
    return xmax
        