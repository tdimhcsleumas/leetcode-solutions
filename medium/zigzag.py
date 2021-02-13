class Solution:
    def convert(self, s: str, numRows: int) -> str:
        idx = 0
        mat = [""] * numRows;
        
        direction = 1
        
        while idx < len(s):
            elements = range(0, numRows) if direction > 0 else range(numRows-2, 0, -1)
            
            for i in elements:
                if idx >= len(s):
                    break
                mat[i] += s[idx]
                idx += 1
                
            direction *= -1
                            
        return "".join(mat)
