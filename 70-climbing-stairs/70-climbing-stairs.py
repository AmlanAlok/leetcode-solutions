class Solution:
    def climbStairs(self, n: int) -> int:
        return self.ans2(n)
    
    '''
    dynamic
    TC = 2^n
    SC = m+m = 2m = m
    '''
    def ans1(self, n: int, memo = {}) -> int:
    
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        
        ans = self.ans1(n-1) + self.ans1(n-2)
        
        memo[n] = ans
        return ans
    
    
    def ans2(self, n: int) -> int:
        
        if n < 3:
            return n
        
        a = [None]*(n+1)
        a[1] = 1
        a[2] = 2
        
        for i in range(3, len(a)):
            a[i] = a[i-1] + a[i-2]
            
        return a[n]
        
        