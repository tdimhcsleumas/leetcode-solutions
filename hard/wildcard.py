from functools import cache
class Solution:
    def match(self, s: str, p: str) -> bool:
        return p == "." or p == s
    
    @cache
    def _isMatch(self, s: str, p: str, i, j) -> bool:

        if len(s) == i and len(p) == j:
            ans = True
        elif j < len(p) - 1 and p[j+1] == '*':
            ans = self._isMatch(s, p, i, j+2)
            k = i
            
            while k < len(s) and self.match(s[k], p[j]):
                ans = ans or self._isMatch(s, p, k+1, j+2)
                k = k + 1
        elif bool(len(s) == i) != bool(len(p) == j):
            ans = False
        else:
            ans = self.match(s[i], p[j]) and self._isMatch(s, p, i+1, j+1)
            
        return ans
    
    
    def isMatch(self, s: str, p: str) -> bool:
        return self._isMatch(s, p, 0, 0)
