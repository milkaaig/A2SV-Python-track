class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
       
        siz1 = len(word1)
        siz2 = len(word2)
        output = ''
        i = 0
        j = 0
        
        while i < siz1 and j < siz2:
            if word1[i] > word2[j]:
                output += word1[i]
                i += 1
            elif  word1[i] < word2[j]:
                output += word2[j]
                j += 1
            elif word1[i] == word2[j]:
                if word1[i: ] > word2[j: ]:
                    output += word1[i]
                    i += 1
                elif word1[i: ] <= word2[j: ]:
                    output += word2[j]
                    j += 1
                
        output += word1[i: ] + word2[j: ]
        
        return output
                