# "III"
# "LVIII"
# "MCMXCIV"
class Solution:
    def romanToInt(self, s: str) -> int:
        return self.ans2(s)
    
    '''
    TC = O(1) and not O(n) bcuz the max possible number is 3999 as given here.
    SC = O(1)
    '''
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
        
        for i in range(len(s)-2, -1, -1):
            
            c = s[i]
            if c in d:
                
                v = d[c]
                
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
                
        
    '''
    TC = 1
    SC = 1
    This approach is much better and optimized
    '''
    def ans2(self, s: str) -> int:
        d = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000
            }
        
        last = len(s)-1
        total = d[s[last]]
        
        for i in range(len(s)-2, -1, -1):
            if d[s[i]] < d[s[i+1]]:
                total -= d[s[i]]
            else:
                total += d[s[i]]
        
        return total

                
                
            
            
        