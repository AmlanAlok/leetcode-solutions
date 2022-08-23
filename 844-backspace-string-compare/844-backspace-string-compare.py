'''
"xywrrmp"
"xywrrmu#p"
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
        return ans1(s, t)

    
def ans2(s, t):
    
    if len(t) > len(s):
        s, t = t, s
    i, j = 0, 0
    es, et = 0, 0
    
    
    while i < len(s) and j < len(t):
        
        if s[i] == '#':
                if es == 0:
                    while s[i] =='#' and i < len(s):
                        i+=1
                else:
                    while es > 0 and s[i] == '#' and i < len(s):
                        es-=1
                        i+=1
        if t[j] == '#':
                if et == 0:
                    while t[j] == '#' and j < len(t):
                        j+=1
                else:
                    while et > 0 and t[j] == '#' and j < len(t):
                        et-=1
                        j+=1
                        
        if i < len(s) and j < len(t) and s[i] != t[j]:
            es+=1
            et+=1
        
        i+=1
        
        if j+1 < len(t):
            j+=1
        
                
    print(es, et)
    if es ==0 and et == 0:
        return True
    return False
                


'''
TC = n+m
SC = n or m, which is greater
'''
def ans1(s, t):
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




'''From LC Solutions'''

def ans9():
    def f(string, pointer):
            cnt = 1 
            pointer -= 1
            while cnt > 0:
                if pointer == -1:
                    return pointer
                if string[pointer] == '#':
                    cnt += 1
                else:
                    cnt -= 1
                pointer -= 1
            return max(-1, pointer)
        
    l = len(s) - 1
    r = len(t) - 1
    while l > -1 and r > -1:
        if s[l] == '#' or t[r] == '#':
            while s[l] == '#':
                l = f(s, l)
                if l == -1:
                    break
            while t[r] == '#':
                r = f(t, r)
                if r == -1:
                    break
        else:
            if s[l] == t[r]:
                l -= 1
                r -= 1
            else:
                return False
    if l <= -1 and r <= -1:
        return True
    if l <= -1:
        if t[r] != '#':
            return False
        while True:
            r = f(t, r)
            if r == -1:
                return True
            if t[r] != '#':
                return False
    else:
        if s[l] != "#":
            return False
        while True:
            l = f(s, l)
            if l == -1:
                return True
            if s[l] != '#':
                return False
