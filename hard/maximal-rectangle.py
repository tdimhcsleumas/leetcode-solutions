class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:     

        if not matrix: return 0
        
        def mah(nums):
            nums+=[0]
            stack=[(-1,-1)]
            ans=0

            for i in range(len(nums)):
                while nums[i]<stack[-1][1]:
                    (_,h)=stack.pop()
                    w=i-stack[-1][0]-1
                    ans=max(ans,w*h)
                stack.append((i,nums[i]))
            return ans
        
        m = len(matrix)
        n = len(matrix[0])
        
        dp = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i][j] = 1 if matrix[i][j] == '1' else 0
                else:
                    dp[i][j] = dp[i-1][j] + 1 if matrix[i][j] == '1' else 0
                        
        print(dp)
        ans = 0
        for i in range(m):
            ans = max(ans, mah(dp[i]))
            
        return ans
            
