# 123
# 12345
# 2147483647
# 1234567891
# 0
# 20
# 10
# 100
# 1000

class Solution:
    def numberToWords(self, num: int) -> str:
        return self.ans1(num)
    
    def ans1(self, num: int) -> str:
        
        if num == 0:
            return 'Zero'
        
        n = num
        ans = []
        nums = []
        titles = [' Billion' ,' Million',' Thousand' ,'']
        
        while n > 0:
            p = n%1000
            nums.insert(0, p)
            n = n // 1000
            
        for i in range(len(nums)-1, -1, -1):
            number = nums[i]
            eng = self.three(number)
            if eng != '':
                ans.insert(0, self.three(number) + titles.pop())
            else:
                titles.pop()
            # print(len(self.three(number))
        
        # print(ans)
        return ' '.join(ans)
        
    
    def three(self, n: int):
        
        one_d = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
        two_d = {1:'One', 2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}
        ele_d = {10: 'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}
        
        st = []
        nums = []
        n2 = n
        
        while n>0:
            p = n%10
            nums.append(p)
            n = n//10
            
        # print(nums)
        
        i = 1
        
        while i<=len(nums):
            
            if i == 2 and nums[1] == 1:
                if st:
                    st.pop()
                st.insert(0, ele_d[n2%100])
            elif i == 2 and nums[i-1] != 0:
                st.insert(0, two_d[nums[i-1]])
            elif i == 1 and nums[i-1] != 0:
                st.insert(0, one_d[nums[i-1]])
            elif i == 3 and nums[i-1] != 0:
                st.insert(0, one_d[nums[i-1]] + ' Hundred')
                
            i+=1
        
        print('three')
        print(st)
        
        return ' '.join(st)
                    