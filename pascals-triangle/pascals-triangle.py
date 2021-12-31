class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        return self.ans_1(numRows)
        
        
    def ans_1(self, numRows: int) -> List[List[int]]:
        
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
                
    
        