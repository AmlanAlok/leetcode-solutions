'''
"ab#c"
"ad#c"
"ab##"
"c#d#"
"a#c"
"b"
"a##c"
"#a#c"
'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        return p(s) == p(t)
        

def p(s):

    n = []
    i=0
    while i<len(s):
        if s[i] == '#':
            if len(n) > 0:
                n.pop()
        else:
            n.append(s[i])
            
        i+=1

    return n
        
        