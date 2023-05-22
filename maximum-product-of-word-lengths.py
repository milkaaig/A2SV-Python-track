class Solution:
    def maxProduct(self, words: List[str]) -> int:
        
        n = len(words)
        maxm = 0
        for i in range(n):
            a = set(words[i])
            for j in range(i + 1, n):
                b = set(words[j])
                val = len(set(a.intersection(b)))
                if val == 0:
                    maxm = max(maxm, len(words[i]) * len(words[j]))
        
        return maxm