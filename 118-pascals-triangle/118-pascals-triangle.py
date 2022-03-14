class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.ans2(numRows)
    
        
    def ans1(self, numRows: int) -> List[List[int]]:
        
        ans = []
        
        for i in range(1,numRows+1):
            
            if i == 1:
                ans.append([1])
            if i == 2:
                ans.append([1, 1])
            if i > 2:
                a = [1]
                for j in range(i-2):
                    a.append(ans[i-2][j] + ans[i-2][j+1])
                a.append(1)
                ans.append(a)
        
        print(ans)
        return ans
        
    def ans2(self, numRows: int) -> List[List[int]]:
        
        n = numRows
        a = []
        
        if n>=1:
            a.append([1])
        if n>=2:
            a.append([1,1])
        
        i=3
        
        while i<=n:
            
            x = [None]*i
            x[0], x[-1] = 1, 1
            
            j=1
            
            while j<(len(x)-1):
                x[j] = a[i-2][j] + a[i-2][j-1]
                j+=1
                
            a.append(x)
            i+=1
        
        return a
        
    
        