'''
[2,7,11,15]
9
[1,2,3,7,3]
6
[3,3]
6
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        return self.p3(nums, target)
    
    def ans_1(self, nums: List[int], target: int) -> List[int]:
        
        dict = {v:i for i,v in enumerate(nums)}
        
        for i in range(len(nums)):
            
            c = target-nums[i]
            if c in dict and i is not dict[c]:
                return [i, dict[c]]
            
        return False
        
    def p1(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i,v in enumerate(nums):
            
            c= target-v
            
            if c in d and d[c] != i:
                return [i, d[c] ]
            else:
                d[v] = i
        
        return []
            
    def p2(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        
        for i in range(nums):
            
            c= target-v
            
            if c in d and d[c] != i:
                return [i, d[c] ]
            else:
                d[v] = i
        
        return []
    
    '''
    TC = n
    SC = n
    '''
    def p3(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        t = target
        
        for i,v in enumerate(nums):
            c = t-v
            if c in d and d[c] != i:
                return [i,d[c]]
            else:
                d[v]=i
        
        return [-1,-1]
            
            
    