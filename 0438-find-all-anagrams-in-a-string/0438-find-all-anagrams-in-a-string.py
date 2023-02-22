from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p = Counter(p)
        window = s[:k]
        cwindow = Counter(window)
        output = []
        
        i = k 
        while i <= len(s):
            if p == cwindow:
                output.append(i - k)
                
            if i >= len(s):
                break
                
            window += s[i]
            window = window[1:]
            cwindow = Counter(window)
            i += 1
        
        
            
        return output