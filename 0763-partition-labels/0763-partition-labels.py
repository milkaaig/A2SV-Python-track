class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mapp = {}
        size = len(s)
        #last index of char(last seen index)
        for i in range(len(s)):
            mapp[s[i]] = i
        
        
        #compares lenght of s[i] and e append if i = e and restars the size
        output = []
        l = 0
        r = mapp[s[0]]
        
        for i in range(size):
            r = max(r, mapp[s[i]])
            
            if i == r:
                leng = r - l + 1
                output.append(leng)
                l = r + 1
            
        
        return output
            