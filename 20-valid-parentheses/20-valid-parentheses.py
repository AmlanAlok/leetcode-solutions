from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        
        return self.p2(s)
    
    def ans1(self, s: str) -> bool:
        
        a=deque()
        
        for v in s:
            
            if a:
                if v==')' and a[-1] == '(' or v=='}' and a[-1]=='{' or v == ']' and a[-1]=='[':
                    a.pop()
                    continue
            
            a.append(v)
            
        return len(a)==0
    
    def p1(self, s: str) -> bool:
        
        a = []
        
        for i in s:
            
            if a:
                if (i == '}' and a[-1] == '{') or (i == ')' and a[-1] == '(') or (i == ']' and a[-1] == '['):
                    a.pop()
                    continue
            
            a.append(i)
        
        return len(a)==0

    def p2(self, s: str) -> bool:
        
        a=deque()
        
        for i in range(len(s)):
            # print(i)
            x = s[i]
            
            if a:
                if i>0 and ( (x==')' and a[-1]=='(') or 
                            (x=='}' and a[-1]=='{') or 
                            (x==']' and a[-1]=='[') ):
                    a.pop()
                    continue
                
            a.append(x)
            pass
            
        return len(a)==0
            
        
        