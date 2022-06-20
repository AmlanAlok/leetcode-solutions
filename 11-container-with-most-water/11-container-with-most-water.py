class Solution:
    def maxArea(self, height: List[int]) -> int:
        return self.ans1(height)
    
    def ans1(self, height: List[int]) -> int:
        
        i = 0
        j = len(height)-1
        
        maxv = -1
        
        while i<j:
            # print(i, j)
            w = j-i
            h = min(height[i], height[j])
            
            area = w*h
            
            if area > maxv:
                maxv = area
                
            if height[i] < height[j]:
                temp = height[i]
                while height[i] <= temp and i<j:
                    i += 1
            else:
                temp = height[j]
                while height[j] <= temp and i<j:
                    j -= 1
        
        return maxv
            
        
        
        
        
        
        
    
    