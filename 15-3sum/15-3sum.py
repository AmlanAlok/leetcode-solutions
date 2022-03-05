class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        return self.ans1(nums)
    
    def ans1(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []
        
        nums.sort()
        ans = []
        m = nums[0]-1
        
        for k in range(len(nums)-2):
            
            if nums[k]==m:
                continue
                
            i = k+1
            j=len(nums)-1
            
            mi = nums[i]
            mj=nums[j]
            
            while i<j:
                # print(nums[k])
                
                
                s = nums[i]+nums[j]+nums[k]
                
                if s<0:
                    i+=1
                elif s>0:
                    j-=1
                else:
                    x = [nums[k],nums[i],nums[j]]
                    
                    # if x not in ans:
                    ans.append(x)
                                                   
                    i+=1
                    j-=1
                    
                    while i<j and nums[i]==nums[i-1]:
                        i+=1                    

            m = nums[k]
                
        return ans
        

    def fail1(self, nums: List[int]) -> List[List[int]]:
        # print('start')
        if nums is [] or nums is [0]:
            return []
        
#         d={v: i for i,v in enumerate(nums)}
        
#         di = d.items()
        
#         print('a')

        d={}
        a=[]
        
        for i in range(len(nums)):
            
            v = nums[i]
            
            if v in d:
                d[v]+=1               
            else:
                d[v] = 1
        
        # nums.sort()
        
        for i in range(len(nums)):

            q = d.copy()
            di = q.items()
            x = nums[i]

            
            for k, v in di:
                c = x+k
                c = -1*c
                
                if c in q and q[c]>0 and q[k]>0 and q[x]>0:
                    
                    q[c]-=1
                    q[k]-=1
                    q[x]-=1

                    if [x,k,c] not in a and q[c]>=0 and q[k]>=0 and q[x]>=0:
                        
                        ins = True
                        for e in a:
                            if x in e and k in e and c in e:
                                ins = False
                        if ins:
                            a.append([x,k,c])

        return a