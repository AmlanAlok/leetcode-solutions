class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.p1(prices)
    
    def ans_1(self, prices: List[int]) -> int:
        
        b = 0
        s = 0
        m = 0
        
        for i in range(1, len(prices)):
            
            p = prices[i] - prices[b]
            
            if p > 0:
                if p > m:
                    m = p
            
            if p < 0:
                b = i
                
        return m
    
    def p1(self, prices: List[int]) -> int:
        
        nums = prices
        m=0
        b=0
        s=0
        
        for i in range(len(prices)):
            
            p = nums[i]-nums[b]
            
            if p > 0 and p > m:
                    m=p
            if p<0:
                b=i
            
        return m
        
        
        