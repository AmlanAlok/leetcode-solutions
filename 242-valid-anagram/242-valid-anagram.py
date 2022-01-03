class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return self.ans_2(s,t)
        
    # TC = O(n+m)
    # SC = O(n+m)
    # Runtime: 24 ms, faster than 99.89% of Python3 online submissions for Valid Anagram.
    def ans_2(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        
        d = collections.Counter(t)
        a = collections.Counter(s)
        
        if a != d:
            return False
        return True
    
    # TC = O(n+m)
    # SC = O(m)
    def ans_1(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        d = collections.Counter(t)
        
        for i in s:
            if i not in d:
                return False
            
            if d[i] <= 0:
                return False
            
            d[i] -= 1
            
        return True
            
            
        