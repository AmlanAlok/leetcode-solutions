class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return ans1(nums)
    
    
def ans1(nums):
    
    i, j = 0, len(nums)-1
    
    ans = [None] * len(nums)
    k = len(nums)-1
    
    while i <= j:
        
        left, right = abs(nums[i]), abs(nums[j])
        
        if right > left:
            ans[k] = right**2
            j-=1
        else:
            ans[k] = left**2
            i+=1
        k-=1
        
    return ans
    