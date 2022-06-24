'''
[-2,1,-3,4,-1,2,1,-5,4]
[5,4,-1,7,8]
[1]
[1,2]
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.p1(nums)
    
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

    def p1(self, nums: List[int]) -> int:
        
        maxv = -sys.maxsize
        csum = 0
        
        for i in nums:
            
            if i+csum < i:
                csum = i
            else:
                csum += i
                
            if csum > maxv:
                maxv = csum
            
        return maxv
            
        
        