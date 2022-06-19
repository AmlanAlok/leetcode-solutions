class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.ans1(strs)
    
    def ans1(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        common = strs[0]
        
        i = 1
        
        while i< len(strs):
            
            j = strs[i].find(common)
            
            if j == 0:
                # print('match')
                i+=1
            else:
                common = common[:len(common)-1]
                
        return common
        
        