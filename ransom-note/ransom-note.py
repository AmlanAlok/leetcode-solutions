from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return self.ans_1(ransomNote, magazine)
        
    def ans_1(self, ransomNote: str, magazine: str) -> bool:
        
        dict = Counter(magazine)
        print(dict)
        
        for i in ransomNote:
            if i in dict:
                if dict[i] > 0:
                    dict[i] -= 1
                else:
                    return False
            else:
                return False
            
        return True
                
        