from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.ans1(s, t)
    
    
    '''
    TC = n
    SC = n+m
    '''
    def ans1(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
            
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
    
    def ans2(self, s: str, t: str) -> bool:
        source = Counter(s)
        target = Counter(t)
        print(source)
        print(target)
        return True if source == target else False
                
        