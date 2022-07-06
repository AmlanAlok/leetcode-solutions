class Solution:
    def fib(self, n: int) -> int:
        return ans2(n)
    
def ans1(n):
    
    a = [None]*(n+1)
    
    if n >= 0:
        a[0] = 0
    if n >= 1:
        a[1] = 1
    
    i = 2
    
    while i < n+1:
        a[i] = a[i-1] + a[i-2]
        i+=1
        
    return a[n]

def ans2(n, memo={}):
    
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    memo[n] = ans2(n-1, memo) + ans2(n-2, memo)
    
    return memo[n] 
    
    
        
        