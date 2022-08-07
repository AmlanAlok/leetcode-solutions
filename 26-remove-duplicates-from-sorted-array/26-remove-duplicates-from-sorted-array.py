class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return ans1(nums)
    
def ans1(nums):
    
    i, j = 0, 1
    l = len(nums)
    
    while i < l and j < l:
        
        if nums[j] != nums[i]:
            i+=1
            nums[i] = nums[j]
        j+=1
        
    return i+1
        
        
    

        