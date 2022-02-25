class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        return self.ans1(numbers, target)
    
    def ans2(self, numbers: List[int], target: int) -> List[int]:
        
        nums = numbers
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