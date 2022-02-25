class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        return self.ans3(numbers, target)
    
    
    def ans3(self, numbers: List[int], target: int) -> List[int]:
        
        nums=numbers
        i=0
        j=len(nums)-1
        
        while i<j:
            s=nums[i]+nums[j]
            
            if s>target:
                j-=1
            elif s<target:
                i+=1
            else:
                return [i+1, j+1]
            
        return [-1,-1]
    
    '''
    This solution does not work. It is incorrect.
    '''
    def ans2(self, numbers: List[int], target: int) -> List[int]:
        
        nums = numbers
        
        for i in range(len(nums)):
            if nums[i] == target:
                if i+1<len(nums) and nums[i]+nums[i+1] == target:
                    print('does not work')
        
        
        i=0
        j=0
        while nums[i]<target:
            while nums[j]<target:

                if nums[i]+nums[j] == target:
                    return [i+1, j+1]
                j+=1
            i+=1
        
        
    '''
    TC = O(n)
    Sc = O(n)
    '''
    def ans1(self, numbers: List[int], target: int) -> List[int]:
        
        d={}
        nums=numbers
        
        for i in range(len(nums)):
            
            v = nums[i]
            c = target-v
            if c in d:
                return [d[c]+1,i+1]
            else:
                d[v] = i