from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
       
       
        dics1 = defaultdict(int)
        
        for i  in range(len(s1)):
            dics1[s1[i]] += 1
        
        windic = defaultdict(int)
        
        for i in range(len(s1)):
            windic[s2[i]] += 1
        
        if dics1 == windic:
            return True
        
        start = len(s1)
        
        for i in range(start , len(s2)):
            
            windic[s2[i - len(s1)]] -= 1
            
            if windic[s2[i - len(s1)]] == 0:
                windic.pop(s2[i - len(s1)])
                
            windic[s2[i]] += 1
            
            if dics1 == windic:
                return True
        
            
        return False
      