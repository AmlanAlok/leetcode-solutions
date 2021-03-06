from collections import deque

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        return self.ans3(s)
    
    # my atempt - very inefficient
    def ans1(self, s: str) -> str:
        
        a=deque()
        b=deque()
        ans=[]
        
        for i, c in enumerate(s):
            
            if a and c==')' and a[-1]=='(':
                a.pop()
                b.pop()
                continue
            elif c=='(' or c==')':    
                a.append(c)
                b.append(i)
            
        if len(a)==0:
            return s

        # for i,v in enumerate(b):
            # if i>=1:
            #     # v=v-b[i-1]
            #     v=v-1
            # s = s[:v] + s[v+1:]
            # s[i] = '.'
        for i, v in enumerate(s):
            
            if i not in b:
                ans.append(v)
            
            
        print(ans)

        return ''.join(ans)
                      
    '''
    My attempt at a more efficient solution - copy of ans3
    '''
    def ans2(self, s: str) -> str:
        
        a=[]
        x=list(s)
        
        for i,v in enumerate(x):
            
            if v=='(':
                a.append(i)
            if v==')':
                if a:
                    a.pop()
                else:
                    x[i]=''
            
        while a:
            i = a.pop()
            x[i]=''
            
        return ''.join(x)
                  
    '''
    60 ms ans from LC
    '''
    def ans3(self, s: str) -> str:
        
        if not s:
            return None
        
        stack = []
        char_array = list(s)
        
        for idx, char in enumerate(s):
            if char == ")":
                if stack:
                    stack.pop()
                else:
                    char_array[idx] = ""
            elif char == "(":
                stack.append(idx)
        
        while stack:
            idx = stack.pop()
            char_array[idx] = ""
        
        return "".join(char_array)
            
            
            
            
            
            
            
            
            
            
            
            