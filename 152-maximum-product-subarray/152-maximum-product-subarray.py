class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.ans1(nums)
    
    def ans1(self, nums: List[int]) -> int:
        
        amax, amin = nums[0], nums[0]
        ans = amax
        
        for i, n in enumerate(nums):
            
            if i == 0:
                continue
            new_max = amax*n
            new_min = amin*n
            
            amax = max(n, new_max, new_min)
            amin = min(n, new_max, new_min)
            
            ans = max(ans, amax)
            
        return ans
            
            
            
            
            
            
                
            
        
    
    
    def failed_attempt(self, nums: List[int]) -> int:
        
        m = -sys.maxsize
        a = 1
        zf = True
        
        for i in range(len(nums)):
            
            n = nums[i]
            if n == 0 and zf:
                a = 1
                continue
            
            zf = False
            a *= n
            
            # if a < n:
            #     a = n
            if m < a:
                m = a
        
        if m == -sys.maxsize:
            m = 0
        return m