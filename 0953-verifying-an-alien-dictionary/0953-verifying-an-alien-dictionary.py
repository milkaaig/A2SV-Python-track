class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dicw = {}
        for i in range(len(order)):
            dicw[order[i]] = i
        maxlen = 0
        
        y = len(words)
        for i in range(y -1):
            x = len(words[i])
            for j in range(x):
                if  j >= len(words[i+1]):
                    return False
                
                if words[i ][j] != words[i +1][j]:
                    if dicw[words[i ][j]] > dicw[words[i +1][j]]:
                        return False
                    break
        return True
                    
                
            