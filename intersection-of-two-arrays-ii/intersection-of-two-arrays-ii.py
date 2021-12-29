class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        return self.ans_2(nums1, nums2)
    
# TC = O(n log n + m log m + m + n) = O(n log n + m log m)
#   sorting TC = n log n
#   Python's built in sort method is a spin off of merge sort called Timsort, more information here - https://en.wikipedia.org/wiki/Timsort
#   It's essentially no better or worse than merge sort, which means that its run time on average is O(n log n) and its space complexity is Ω(n)
# SC = O(n+m), if already sorted, then SC = O(1)
    def ans_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1.sort()
        nums2.sort()
        
        print(nums1)
        print(nums2) 
        
        i=0
        j=0
        k=0
        
        while i<len(nums1) and j<len(nums2):
            
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2 [j]:
                j += 1
            else:
                nums1[k] = nums1[i]
                i += 1
                j += 1
                k += 1
        
        return nums1[:k]
        
    
# TC = O(n+m)
# SC = O(min(n, m))
    def ans_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if len(nums1) > len(nums2):
            return self.ans_1(nums2, nums1)
        
        dict = {}
        k = 0
        
        for i, v in enumerate(nums1):
            if v in dict:
                dict[v] += 1
            else:
                dict[v] = 1
                
        print(dict)
        
        
        for i, v in enumerate(nums2):
            if v in dict and dict[v] > 0:
                nums1[k] = v
                k += 1
                dict[v] -= 1
        
        return nums1[:k]
