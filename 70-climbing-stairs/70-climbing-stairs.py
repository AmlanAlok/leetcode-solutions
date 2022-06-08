class Solution:
    def climbStairs(self, n: int) -> int:
        return self.ans4(n)
    
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
    
    '''
    table
    TC = n
    SC = n
    '''
    def ans2(self, n: int) -> int:
        
        if n < 3:
            return n
        
        a = [None]*(n+1)
        a[1] = 1
        a[2] = 2
        
        for i in range(3, len(a)):
            a[i] = a[i-1] + a[i-2]
            
        return a[n]
    
    '''
    Fibonnacci Number
    TC = n
    SC = 1
    '''
    def ans3(self, n: int) -> int:
        
        prev, current = 1, 1
        
        for i in range(n-1):
            prev, current = current, prev + current
    
    '''
    Fibonnacci Number
    TC = n
    SC = 1
    '''
    def ans4(self, n: int) -> int:
        if n == 1:
            return 1
        prev, current = 1, 2 
        
        for i in range(2, n):
            temp = current
            current = current + prev
            prev = temp
        
        return current
        
        