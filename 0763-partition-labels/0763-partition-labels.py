class Solution:
    def partitionLabels(self, s: str) -> List[int]:
#         Painful gruelling so painful
        mapp = {}
        size = len(s)
        for i in range(size):
            mapp[s[i]] = i
            
        output = []
        l = 0
        r = mapp[s[0]]
        
        for i in range(size):
            r = max(r, mapp[s[i]])
            if i == r:
                output.append(r - l + 1)
                l = r + 1
            
        return output
        
        
            