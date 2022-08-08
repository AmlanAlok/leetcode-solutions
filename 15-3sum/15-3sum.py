'''
[-1,0,1,2,-1,-4]
[0,1,1]
[0,0,0]
[-1,0,1,2,-1,-4,2]
[-4,2,2]
[0,0,0,0]
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        return self.ans1(nums)
    
    '''
    A1 - 2 pointers
    This approach is the fastest as it skips duplicates
    '''
    def ans1(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0:
            return []
        
        nums.sort()
        ans = []
        m = nums[0]-1   # so that there is no match
        
        for k in range(len(nums)-2):
            
            if nums[k]==m:      # this helps to skip duplicates
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
                    
                    # if x not in ans:  # this line was adding a lot of TC. removing this lowered time from 4000ms to 700ms
                    ans.append(x)
                                                   
                    i+=1
                    j-=1
                    
                    # this helps to skip duplicates
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
    
    '''
    Approach 2 - Using hashmap
    '''
    def ans2(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        print(nums)
        l = len(nums)
        ans=[]
        k=0
        
        # for k in range(l):
        while k<l-2:
            
            i = k+1
            
            d={}
            
            while i<l:
                
                c = -1*nums[k] - nums[i]
                
                if c in d:
                    ans.append([nums[k],c,nums[i]])
                    
                    # i+=1
                    
                    # if i<l and nums[i]==nums[i-1]:
                    #     while i<l and nums[i]==nums[i-1]:
                    #         i+=1
                    if i<l-1 and nums[i]==nums[i+1]:
                        while i<l-1 and nums[i]==nums[i+1]:
                            i+=1
                            
                else:
                    d[nums[i]] = i
                
                i+=1
                    
                
                # We cannot do this bcuz [-4,2,2], as i and j can have the same value in ans, we cannot skip repeating values when scanning through the array
                
                # if i<l and nums[i]==nums[i-1]:
                #     while i<l and nums[i]==nums[i-1]:
                #         i+=1
            
            k+=1
            
            if nums[k]==nums[k-1]:
                while k<l-2 and nums[k]==nums[k-1]:
                    k+=1
        
        return ans
    '''
    A3 - If sorting is not allowed, how will you track and manage duplication
    '''
    def ans3(self, nums: List[int]) -> List[List[int]]:
        
        
        l = len(nums)
        ans=set()
        d1={}
        d3={}
        
        for k in range(l-2):
            
            if nums[k] not in d1:
                
                d1[nums[k]]=k
                i=k+1
                d2={}
                
                while i<l:

                    c = -1*nums[k] - nums[i]

                    if c in d2 and d2[c] != i:
                        # x = [nums[k],c,nums[i]]
                        # x.sort()

                        # if x not in d3:
                        # ans.append(x)
                        
                        # This is a very important trick
                        x = (nums[k],c,nums[i])
                        ans.add(tuple(sorted(x)))

                    else:
                        d2[nums[i]]=i
                    
                    i+=1
                    
                
                
            # else:
            #     d1[nums[k]]=k
        return ans
    
    
    '''
    Test Cases
    [-1,0,1,2,-1,-4,2]
    [-4,2,2]
    [0,0,0]
    [0,0,0,0]
    
    How to track duplicate lists in a set?
    x = (nums[k],c,nums[i])
    ans.add(tuple(sorted(x)))
    '''
    
    
    '''
    TypeError: unhashable type: 'list'
    '''
    '''
    TC = n^2
    SC = n
    '''
    def p1(self, nums: List[int]) -> List[List[int]]:
        
        i = 0
        n = len(nums)
        ans = set()
        
        while i < n:
            
            d1 = {}
            j = 0
            
            while j < n and i != j:
                
                c = (nums[i]+nums[j])*-1
                
                if c in d1 and d1[c] != i and d1[c] != j:
                    ans.add(tuple(sorted([nums[i], nums[j], c])))
                else:
                    d1[nums[j]]=j
                
                j+=1
            
            i+=1
            
        return list(ans)
        
    
    