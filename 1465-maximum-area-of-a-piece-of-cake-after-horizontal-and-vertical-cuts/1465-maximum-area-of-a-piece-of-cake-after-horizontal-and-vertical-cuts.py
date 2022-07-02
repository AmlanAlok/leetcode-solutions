'''
1000000000
1000000000
[2]
[2]
5
4
[1,2,4]
[1,3]
5
4
[3,1]
[1]
5
4
[3]
[3]
'''
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        return ans1(h, w, horizontalCuts, verticalCuts)
    
'''
TC = n + n log n
SC = 1
'''
def ans1(h, w, hnums, vnums):
    
    hmax = vmax = 0
    
    if not hnums:
        hmax = h
    if not vnums:
        vmax = w    
    # if hmax != 0 and vmax != 0:
    #     return hmax*vmax
    if hmax == 0:
        hnums.sort()
        hnums.append(h)
        hmax = get_max(hnums)
    if vmax == 0:
        vnums.sort()
        vnums.append(w)
        vmax = get_max(vnums)
    
    print(hmax, vmax)
    return (hmax*vmax)%(pow(10, 9)+7)
    
    
def get_max(nums):
    
    xmax = nums[0]
    i = 1 # 2nd pos
    
    while i < len(nums):
        
        diff = nums[i] - nums[i-1]
        
        if diff > xmax:
            xmax = diff
        i += 1
    
    return xmax
            
    