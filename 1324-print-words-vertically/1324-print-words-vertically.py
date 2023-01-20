class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        colum = len(max(s, key = len))
        output = []
        
        for i in range(colum):
            pout = []
    
            for word in s:
                if i >= len(word):
                    pout.extend(" ")
                else:
                    pout.extend(word[i])
                    
            pout = "".join(pout).rstrip()
            output.append(pout)
        return output