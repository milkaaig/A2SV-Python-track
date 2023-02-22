from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k = len(p)
        p = Counter(p)
        cwindow = Counter(s[: k])
        output = []
        
        i = k 
        while i <= len(s):
            if p == cwindow:
                output.append(i - k)
            if i >= len(s):
                break
                
            cwindow[s[i - k]] -= 1
            
            if cwindow[s[i - k]] == 0:
                del cwindow[s[i - k]]
                
            cwindow[s[i]] += 1

            i += 1
        
        
            
        return output