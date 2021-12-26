class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        self.ans_1(nums1, m, nums2, n)
    
    
    def ans_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # for i, num in enumerate(nums):
        for i in range(n):
            nums1[m+i] = nums2[i]
            
        nums1.sort()
            
            