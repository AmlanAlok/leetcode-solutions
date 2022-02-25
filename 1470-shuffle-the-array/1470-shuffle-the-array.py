class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        return self.ans2(nums, n)
    
    def ans2(self, nums: List[int], n: int) -> List[int]:
        from collections import deque
        
        i=1
        j=n
        
        t=deque()

        while i<2*n-1:
            c = nums[i]
            
            if c != -1:
                t.append(c)
            # from x
            if i%2 == 0:
                nums[i] = t.popleft()
            # from y
            else:
                nums[i] = nums[j]
                nums[j]=-1
                j+=1
            i+=1
        
        return nums
        
        
        
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
                