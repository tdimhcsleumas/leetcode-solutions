from collections import defaultdict

class Solution:
            
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        dp = defaultdict(lambda: 0)
        maxval = 0
        
        for i in range(1, len(s)):
            if s[i] == ')' and s[i-1] == '(':
                dp[i] = 2 + dp[i-2]
            elif s[i] == ')' and i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(': 
                dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]
            
            maxval = max(maxval, dp[i])
                    
        return maxval
