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
    
    

# Follow-up Questions

# What if the given array is already sorted? How would you optimize your algorithm?

# We can use either Approach 2 or Approach 3, dropping the sort of course. It will give us linear time and constant memory complexity.
# What if nums1's size is small compared to nums2's size? Which algorithm is better?

# Approach 1 is a good choice here as we use a hash map for the smaller array.
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

# If nums1 fits into the memory, we can use Approach 1 to collect counts for nums1 into a hash map. Then, we can sequentially load and process nums2.

# If neither of the arrays fit into the memory, we can apply some partial processing strategies:

# Split the numeric range into subranges that fits into the memory. Modify Approach 1 to collect counts only within a given subrange, and call the method multiple times (for each subrange).

# Use an external sort for both arrays. Modify Approach 2 to load and process arrays sequentially.

