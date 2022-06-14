class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.ans1(s, t)
    
    def ans1(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        if len(s) > len(t):
            s, t = t, s
            
        d = {}
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
        
        for c in t:
            if c in d and d[c] > 0:
                d[c] -= 1
            else:
                return False
        
        return True
                
        