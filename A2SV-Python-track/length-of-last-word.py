class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        lastSpace = n
        
        
        
        for i in range(n-1, -1, -1): 
            if s[i] != ' ':
                break
            elif s[i] == ' ' and s[i - 1] != ' ':
                lastSpace = i
                break
        
        i = lastSpace - 1
        output = 0
        
        while s[i] != ' ' and i >= 0 :
            output += 1
            i -= 1
            
        return output
        
        
            
        
        
        
        