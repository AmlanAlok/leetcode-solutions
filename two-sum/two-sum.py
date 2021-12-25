class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        return self.ans_1(nums, target)
    
    def ans_1(self, nums: List[int], target: int) -> List[int]:
        
        dict = {v:i for i,v in enumerate(nums)}
        
        for i in range(len(nums)):
            
            c = target-nums[i]
            if c in dict and i is not dict[c]:
                return [i, dict[c]]
            
        return False