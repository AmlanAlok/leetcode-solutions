class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.ans_1(nums1, nums2)
    
    def ans_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        a = set(nums1)
        b = set(nums2)
        
        c = a.intersection(b)
        
        ans = []
        
        ans[:] = c
        
        return ans