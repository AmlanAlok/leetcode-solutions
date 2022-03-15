class Solution:
    
    def simplifyPath(self, path: str) -> str:
        return self.ans1(path)
        
    def fail1(self, path: str) -> str:
        
        s = path
        
        s = s.replace('//','/')
        s = s.replace('.','')
        
        if s[0] != '/':
            s = '/'+s
        
        if s[-1] == '/':
            s = s[:-1]
            
        return s
        
    
    def ans1(self, path: str) -> str:
        
        from collections import deque
        
        s = deque()
        p = path
        
        p = p.split('/')
        
        print(p)
        
        for i, v in enumerate(p):
            
            # if v == '.'
            
            if v == '..' and s:
                s.pop()
                
            elif v == '.' or v == '' or v == '..':
                continue
            
            elif isinstance(v, str):
                s.append(v)
            
        print(s)
                
        return '/'+'/'.join(s)
            
            
            
            
    '''
    Test case
    "/a/./b/../../c/"
    '''
        