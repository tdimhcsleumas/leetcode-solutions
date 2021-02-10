class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        len_max = 0
        
        i = j = 0
        
        while i < len(s):
            if s[i] in window:
                window.remove(s[j])
                j += 1
            else:
                window.add(s[i])
                i += 1
                if (length := len(window)) > len_max:
                    len_max = length
                
                            
        return len_max
                    
                
