class Solution:
    def isValid(self, s: str) -> bool:
        
        return self.ans1(s)
    
    def ans1(self, s: str) -> bool:
        
        from collections import deque
        
        a=deque()
        # b=deque()
        # c=deque()
        # f = True
        
        for i,v in enumerate(s):
            
            if v=='(':
                a.append('(')
            elif v==')':
                if a and a[-1] == '(':
                    a.pop()
                else:
                    return False
                
            elif v=='{':
                a.append('{')
            elif v=='}':
                if a and a[-1] == '{':
                    a.pop()
                else:
                    return False
                
            elif v=='[':
                a.append('[')
            elif v==']':
                if  a and a[-1] == '[':
                    a.pop()
                else:
                    return False
        
        # print(len(a), len(b), len(c))
        if len(a)==0:
            return True
        
        return False
        