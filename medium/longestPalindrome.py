class Solution:
    
    def longestPalindrome(self, s: str) -> str:

        mat = [[False] * len(s) for _ in s]
        B = {1: s[0]}
        
        # init the matrix
        mat[0][0] = True
        for i in range(1, len(s)):
            mat[i][i] = True
            if s[i] == s[i-1]:
                mat[i][i-1] = True
                B[2] = s[i:i+2]
                
        for k in range(1, len(s)):
            for i in range(0, len(s) - k):
                if s[i] == s[i+k] and mat[i+1][i+k-1]:
                    mat[i][i+k] = True
                    B[k+1] = s[i:i+k+1]        
        
        
        return B[max(B.keys())]
