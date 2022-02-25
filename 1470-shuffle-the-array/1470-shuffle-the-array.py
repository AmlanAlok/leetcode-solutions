class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        return self.ans3(nums, n)
    
    '''
    This solution which I did using a queue has constant space
    TC = O(n)
    SC = 2+2(from queue) = O(1)
    '''
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
    
    '''
    TC = O(n)
    SC = n+n+1 =O(n)
    '''
    def ans3(self, nums: List[int], n: int) -> List[int]:
        y=[]
        x=len(nums)//2
        for i in range(x):
            y.append(nums[i])
            y.append(nums[i+n])
        return(y)
        
    '''
    TC = O(n)
    SC = n + n/2 + n/2 + 2 = O(n)
    '''
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
                