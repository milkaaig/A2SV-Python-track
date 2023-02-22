
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        output = ""
        output += s[0]
        long = len(output)
        
        for i in range(1, len(s)):
            
            if s[i] not in output:
                output += s[i]
                long = max(long , len(output) )
               
            else:
                index = output.index(s[i])
                output = output[index + 1:]  + s[i]
               
        return long