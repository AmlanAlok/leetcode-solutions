class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.ans_1(s)
    
    # Horrible code from the comments section. ord function is most likely causing the issue
    def ans_2(self, s: str) -> int:
        
        a = [0]*26
        
        for i in range(len(s)):
            p = ord(s[i]) - ord('a')
            print(p)
            a[p] += 1
        
        for i in range(len(s)):
            p = ord(s[i]) - ord('a')
            print(p)
            if a[p] == 1:
                return i
        
        return -1
        
    
    # TC = O(N)
    # SC = O(1) -> This is not N as english has only 26 alphabets
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
