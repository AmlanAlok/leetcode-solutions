'''
"abcda"
"afgh"
"afabgcdh"
"aabcc"
"dbbca"
"aadbbcbcac"
""
""
""
"aabcc"
"dbbca"
"aadbbbaccc"
"abcd"
"afgh"
"afabgcdh"
"cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
"abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
"abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) == 0 and len(s2) == 0 and len(s3)==0:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
    
        s1 = list(s1)
        s2 = list(s2)
        s3 = list(s3)
        
        memo = {}
        
        # return ans2(s1, s2, s3, len(s1)-1, len(s2)-1, 0)
        return ans2(s1, s2, s3, 0, 0, 0, memo, '')
    
def ans2(s1, s2, s3,i, j, k, memo, z=''):
    
    # print( s1,s2,s3)
    # print(z, i, j, k)
    
    if (i,j) in memo:
        return memo[(i,j)]
    
    if k == len(s3):
        return True
    
    p = []
    
    if k < len(s3):
        if i < len(s1) and s3[k] == s1[i]:
            p.append(ans2(s1, s2, s3, i+1, j, k+1, memo, 'a'))
        if j < len(s2) and s3[k] == s2[j]:
            p.append(ans2(s1, s2, s3, i, j+1, k+1, memo, 'b'))
    else:
        return False
        
    if p and True in p:
        memo[(i,j)] = True
        return True
    else:
        memo[(i,j)] = False
        return False
        
        
    
    
    
    
def ans1(s1, s2, s3):
    
    i, j, k = 0, 0, 0
    n1,n2,n3 = len(s1), len(s2), len(s3)
    
    while k < n3:
    
        if j < n2 and s2[j] == s3[k]:
            j+=1
        elif i < n1 and s1[i] == s3[k]:
            i+=1
        else:
            print(i,j,k)
            return False
        k+=1
        
    return True
        
        