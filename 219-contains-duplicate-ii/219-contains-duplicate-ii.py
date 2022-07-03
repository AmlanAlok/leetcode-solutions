class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        return ans1(nums, k)
    
def ans1(nums, k):
    
    d = {}
    
    for i in range(len(nums)):
        
        n = nums[i]
        
        if n in d:
            if i - d[n] <= k:
                return True
            else:
                d[n] = i
        else:
            d[n] = i
            
    return False
        