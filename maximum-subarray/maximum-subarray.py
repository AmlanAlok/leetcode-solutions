class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        return self.approach_2(nums)
    
    
    def approach_2(self, nums: List[int]) -> int:
        
        m = nums[0]
        a = nums[0]
        
        i = 1
        while i<len(nums):
            
            a = max(nums[i], a+nums[i])   # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            m = max(m, a)
            i += 1
            
        return m
        
        
    
    # TC = O(n2)
    # For nums.length = 10^5, it will give Output limit exceeded
    def approach_1(self, nums: List[int]) -> int:
        m = -math.inf
        
        size = 1
        while size <= len(nums):
            i = 0
            while i < len(nums) and i+size <= len(nums):
                print(nums[i:i+size])
                m = max(m, sum(nums[i:i+size]))
                i +=1
            
            size += 1
        # for i in range(1, len(nums)+1):
        
        return m
        