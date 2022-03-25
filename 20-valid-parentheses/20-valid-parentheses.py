from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        return self.ans2(s)
    
    def ans1(self, s: str) -> bool:
        
        a=deque()
        
        for v in s:
            
            if a:
                if v==')' and a[-1] == '(' or v=='}' and a[-1]=='{' or v == ']' and a[-1]=='[':
                    a.pop()
                    continue
            
            a.append(v)
            
        return len(a)==0
    
    def ans2(self, s: str) -> bool:
        
        a = []
        
        for i in s:
            
            if a:
                if (i == '}' and a[-1] == '{') or (i == ')' and a[-1] == '(') or (i == ']' and a[-1] == '['):
                    a.pop()
                    continue
            
            a.append(i)
        
        return len(a)==0

            
        