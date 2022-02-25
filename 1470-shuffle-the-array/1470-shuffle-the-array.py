class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        return self.ans1(nums, n)
        
    def ans1(self, nums: List[int], n: int) -> List[int]:
        
        x = nums[:n]
        y = nums[n:]
        
        j, k =0, 0
        for i in range(2*n):
            if i%2 == 0:
                nums[i] = x[k]
                k+=1
            else:
                nums[i] = y[j]
                j+=1
                
        return nums
                