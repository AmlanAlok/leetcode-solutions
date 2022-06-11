# "III"
# "LVIII"
# "MCMXCIV"
class Solution:
    def romanToInt(self, s: str) -> int:
        return self.ans1(s)
    
    def ans1(self, s: str) -> int:
        
        d = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
        t = d[s[len(s)-1]]
        ans = 0
        
        for i in range(len(s)-1, -1, -1):
            
            c = s[i]
            if c in d:
                
                v = d[c]
                
                if i == len(s)-1:
                    t = v
                    continue
                
                v2 = d[s[i+1]]
                
                if v2 > v:
                    t -= v
                if v2 == v:
                    t += v
                if v2 < v:
                    ans += t
                    t = v
        ans += t
        
        return ans
                
                
                
                
            
            
        