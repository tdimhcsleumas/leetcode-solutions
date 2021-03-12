class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        heights += [0]
        stack = [-1]
        
        
        # maintain that the element at the bottom of the stack is the smallest
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w=i-stack[-1]-1
                ans = max(ans, w * h)
            stack.append(i)            
            
        return ans
