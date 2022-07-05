'''
[100,4,200,1,3,2]
[0,3,7,2,5,8,4,6,0,1]
[1,2,0,1]
[0]
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return ans2(nums)

'''
TC = n + n = n
SC = n
'''
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

def ans2(nums):
    
    nums = list(set(nums))
    nums.sort()
    
    n = len(nums)
    # print(nums)
    
    if n == 1:
        return n
    
    xmax = 0
    
    l = 1
    i = 1
    
    while i < n:
        
        # v, vp = nums[i], nums[i-1]
        
        while i < n and nums[i] == nums[i-1] + 1:
            l+=1
            # print(l,i)
            i+=1
            
        xmax = max(xmax, l)
        l = 1
        i += 1
            
    return xmax
    
    
    
        