class Solution:
    def intToRoman(self, num: int) -> str:
        return self.ans3(num)
    
    '''
    TC = 1, SC = 1
    '''
    def ans1(self, num: int) -> str:
        n = num
        
        d = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        arr = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        t = []
        
        i = len(arr)-1
        
        while i >=0:
            a = arr[i]
            
            if n >= a:
                n -= a
                t.append(a)
            
            if n < a:
                i -= 1
        
        print(t)
        
        ans=[]
        
        for v in t:
            
            ans.append(d[v])
            
            
        print(ans)
        
        return ''.join(ans)
            
    '''
    TC = 1, SC = 1
    '''
    def ans2(self, num: int) -> str:
        n = num
        
        d = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        
        arr = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        t = ''
        
        i = len(arr)-1
        
        while i >=0:
            a = arr[i]
            
            if n >= a:
                n -= a
                t += d[a]
            
            if n < a:
                i -= 1

        return t
        
    '''
    Tc = 1, Sc = 1
    This approach is much more optimized
    '''
    def ans3(self, num: int) -> str:
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        numeral = ''
        for i in roman:
            # print(i, roman[i])
            numeral += (num // i) * roman[i]
            num %= i
        
        return numeral