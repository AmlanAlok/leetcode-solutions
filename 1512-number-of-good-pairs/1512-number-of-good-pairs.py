class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        return self.ans1(nums)
    
    '''
    TC = O(n)
    SC = O(n)
    This is also the approach for the best time in LC = 16 ms
    '''
    def ans1(self, nums: List[int]) -> int:
        d={}
        p = 0
        
        for i in range(len(nums)):
            
            v = nums[i]
            
            if v in d:
                p+=d[v]
                d[v] +=1
            else:
                d[v] = 1
                
        return p