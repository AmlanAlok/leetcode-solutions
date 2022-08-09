'''
[-1,2,1,-4]
1
[0,0,0]
1
[4,0,5,-5,3,3,0,-4,-5]
-2
[1,1,1,0]
-100
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return ans1(nums, target)
    
def ans1(nums, t):
    
    n = len(nums)
    nums.sort()
    k = 0
    m = sys.maxsize
    closest_sum = sys.maxsize
    prev_k = nums[0]-1
    
    while k < n-2:
        
        if nums[k] == prev_k:
            k+=1
            continue
        
        i = k+1
        j = n-1
        
        while i < j:
            
            s = nums[k] + nums[i] + nums[j]
            
            diff = abs(t-s)
            if diff < m:
                m = diff
                closest_sum = s
                
            if s > t:       # I was comparing with 0
                j-=1
            elif s < t:     # I was comparing with 0
                i+=1
            else:
                return s
            
        prev_k = nums[k]
        k+=1
    
    return closest_sum
        
    