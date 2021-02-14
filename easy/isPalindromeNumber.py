import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        
        mid1 = math.floor((len(s) - 1) / 2)
        mid2 = math.ceil((len(s) - 1) / 2)
        
        while mid1 >= 0 and mid2 < len(s):
            if s[mid1] != s[mid2]:
                return False
            mid1 -= 1
            mid2 += 1
            
        return True
        
