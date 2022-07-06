class Solution:
    def fib(self, n: int) -> int:
        return ans1(n)
    
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
    
        
        