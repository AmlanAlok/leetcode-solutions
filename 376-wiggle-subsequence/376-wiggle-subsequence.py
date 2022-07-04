'''
[1,1,7,4,9,2,5]
[33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
[0,0]
[1,2]
[1]
[1,2,1,2]
[1,1,1,1]
[1,2,1,0,5,3,4]
[1,7,4,9,2,5]
[1,17,5,10,13,15,10,5,16,8]
[1,2,3,4,5,6,7,8,9]
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return ans3(nums)
    
def ans3(nums):
    if len(nums) <= 1:
        return len(nums)

    # find how many times does the non-zero diff changes sign

    ret = 1
    diffSign = 0
    lastNum = nums[0]

    for num in nums:
        if num != lastNum:
            newDiffSign = +1 if num>lastNum else -1
            if newDiffSign != diffSign:
                ret += 1

            diffSign = newDiffSign
            lastNum = num

    return ret
    
def ans2(nums):
    n = len(nums)
    
    if n <= 1:
        return n
    prevdiff = nums[1] - nums[0]
    count = prevdiff = 2 if prevdiff != 0 else 1
    
    for i in range (2, n):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
            count+=1
            prevdiff = diff;
    
    return count
    
    
        
def ans1(nums):
    n = len(nums)
    print(n)

    if n <= 1:
        return n

    a = 0
    xmax = 0
    i = 0
    j=1

    opp = 0
    x = []

    while i<j and j<n:

        c = nums[j]
        p = nums[i]

        diff = c - p

        if diff > 0 and opp != 1:
            a += 1
            opp = 1
            i = j
        elif diff < 0 and opp != -1:
            a+=1
            opp = -1
            i = j
        x.append(opp)
        j+=1
    
    print(x)
    return a+1
        