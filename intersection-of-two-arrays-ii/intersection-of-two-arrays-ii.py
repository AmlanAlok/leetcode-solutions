class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.ans_1(nums1, nums2)
        
    def ans_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        dict = {}
        a = []
        
        for i, v in enumerate(nums1):
            if v in dict:
                dict[v] += 1
            else:
                dict[v] = 1
                
        print(dict)
        
        
        for i, v in enumerate(nums2):
            if v in dict and dict[v] > 0:
                a.append(v)
                dict[v] -= 1
        
        return a
                
        