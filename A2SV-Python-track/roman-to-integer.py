class Solution:
    def romanToInt(self, s: str) -> int:
        val = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        output = 0
        n = len(s)
        i = 0
        
        while i < n:
           
            if i + 1 < n :
                # print(i)
                if (val[s[i]] >= val[s[i + 1]]):
                    output += val[s[i]]
                    i += 1
                else:
                    output += (val[s[i + 1]] - val[s[i]])
                    i += 2
            else:
                
                output += val[s[i]]
                i += 1
                
        
        return output
            