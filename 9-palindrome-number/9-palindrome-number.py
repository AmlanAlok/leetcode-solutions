class Solution:
    def isPalindrome(self, x: int) -> bool:
        return ans1(x)
    
def ans1(num):
    s = str(num)
    return s == s[::-1]
    