class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.ans_1(nums1, nums2)
    
    
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
                
        
                
        
