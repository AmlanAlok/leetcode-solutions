class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.ans_3(s)
    
    # code from solution with fastest time
    def ans_3(self, s: str) -> int:
        
        min_index = len(s)
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            print(c)
            i = s.find(c)       # TC = O(n*m), n = length of string and length of substring to find, returns first positioin, else -1
            x = s.rfind(c)      # TC = O(n*m), n = length of string and length of substring to find, returns last position, else -1
            # print(i, x)
            
            if i != -1 and i == x:
                min_index = min(min_index, i)
        
        return min_index if min_index != len(s) else -1     # This is a neat trick to memorize
    
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
