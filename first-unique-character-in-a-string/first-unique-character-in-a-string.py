class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.ans_1(s)
    
    def ans_1(self, s: str) -> int:
        
        dict = {}
        m = sys.maxsize
        found = False
        
        for i in range(len(s)):
            
            if s[i] in dict:
                dict[s[i]] = sys.maxsize
            else:
                dict[s[i]] = i
                
        for key, value in dict.items():
            print('key =', key, ', value =', value)
            if value < m:
                m = value
                found = True
        
        if found:
            return m
        return -1