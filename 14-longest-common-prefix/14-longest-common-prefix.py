class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        return self.ans3(strs)
    
    '''
    Horizontal scanning
    TC = n
    SC = 1
    '''
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
        
    '''
    Vertical Scanning
    TC = n
    SC = 1
    '''
    def ans2(self, strs: List[str]) -> str:
        
        if len(strs) == 1:
            return strs[0]
        
        ans = ''
        
        common = strs[0]
        
        '''To find the shortest word in the list to reduce computation later'''
        for x in strs:
            if len(common) > len(x):
                common = x
        
        '''Vertical comparision with the shortest word found earlier'''
        for i in range(len(common)):
            
            for x in strs:
                
                if i >= len(x) or x[i] != common[i]:
                    return ans
            
            ans += x[i]
        
        return ans
                
    '''
    Sorting Approach
    TC = nlogn
    SC = 
    '''
    def ans3(self, strs: List[str]) -> str:
        res=''
        n=len(strs)
        strs.sort()     # TC = n log n
        first=strs[0]
        last=strs[n-1]
        for i in range(len(first)):
            if first[i]==last[i]:
                res += first[i]
            else:
                break
        return res 