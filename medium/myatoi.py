import re

class Solution:
    def myAtoi(self, s: str) -> int:
        p = re.compile(r"^\s*([\+-]?\d+).*")
        m = p.findall(s)
        
        if not m:
            return 0
        
        value = int(m[0])
        
        if value < 0:
            return max(value, -pow(2,31))
        else:
            return min(value, pow(2,31)-1)
               
            
        
