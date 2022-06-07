class Solution:
    def climbStairs(self, n: int) -> int:
        return self.ans1(n)
    
    def ans1(self, n: int, memo = {}) -> int:
    
        if n in memo:
            return memo[n]
        if n == 0 or n == 1:
            return 1
        
        ans = self.ans1(n-1) + self.ans1(n-2)
        
        memo[n] = ans
        return ans