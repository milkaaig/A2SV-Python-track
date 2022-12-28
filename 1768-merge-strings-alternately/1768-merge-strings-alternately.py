class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lw1 = len(word1)
        lw2 = len(word2)
        merged = ""
        if lw1 == lw2:
            for letter in range(lw1):
                merged += word1[letter]
                merged += word2[letter]
            return merged
        else:
            if lw1 < lw2:
                for letter in range(lw1):
                    merged += word1[letter]
                    merged += word2[letter]
                merged += word2[lw1 :]
                return merged
            else:
                for letter in range(lw2):
                    merged += word1[letter]
                    merged += word2[letter]
                merged += word1[lw2:]
                return merged