class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.ans1(nums)
    
    '''
    TC = n
    SC = 1
    '''
    def ans1(self, nums: List[int]) -> int:
        
        a = 0
        m = -sys.maxsize
        
        for n in nums:
            a += n
            
            if a < n:
                a = n
            if m < a:
                m = a
        
        return m

            
            
        
        