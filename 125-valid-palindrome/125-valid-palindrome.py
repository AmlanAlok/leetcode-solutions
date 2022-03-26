class Solution:
    def isPalindrome(self, s: str) -> bool:
        return self.ans1(s)
        
    def ans1(self, s: str) -> bool:

        if len(s)==0:
            return False
        
        p=''
        
        for i in s:
            if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90) or (ord(i)>=48 and ord(i)<=57):
                print(ord(i))
                p=p+i
        
        print(p)
        
        p = p.lower()
        print(p)
        
        if len(p)==1:
            if p[0].isalpha():
                return True
            else:
                return False
        
        i, j = 0, len(p)-1

        while i<=j:
            
            if p[i] != p[j]:
                
                return False
            
            i+=1
            j-=1
            
        return True
        