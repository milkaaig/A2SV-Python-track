class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        wordss = list(map(set, words))
        sizeofw = len(wordss)
        j = 0
        for i in range( sizeofw - 1):
            for j in range(1 +i , sizeofw):
               
                if len(wordss[i].difference(wordss[j])) == 0 and      len(wordss[j].difference(wordss[i])) == 0:
                    count += 1
        return count
                    