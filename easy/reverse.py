from math import floor, log10

class Solution:
    def reverse(self, x: int) -> int:
        
        if x == 0: return x
        
        rev = 0
        sign = 1 if x > 0 else -1
        x *= sign
        power = floor(log10(x))
        
        while x != 0 and power >= 0:
            rev += (x % 10) * pow(10, power)
            x //= 10
            power -= 1    
        

        if (sign > 0 and rev > (pow(2, 31) - 1)) or (sign < 0 and rev > pow(2, 31)):
            return 0
                
        return sign * rev
