# from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        right = 0
        window = 0
        counter = {}
        
        while right < len(s):
            
            if s[right] not in counter:
                counter[s[right]] = 0
            counter[s[right]] += 1
            
            window = (right - left) + 1
            
            if window - max(counter.values()) <= k:
                longest = max(longest , window)
                
            else:
                counter[s[left]] -= 1
                left += 1
                
                
            right += 1
            
        return longest
                