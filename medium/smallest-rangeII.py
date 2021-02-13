class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
    
        A.sort()
    
        ans = A[len(A)-1] - A[0]
        
        for i in range(0, len(A) - 1):
            high = max(A[len(A) - 1] - K, A[i] + K)
            low = min(A[0] + K, A[i+1] - K)
            ans = min(ans, high - low)
        
        return ans
        
