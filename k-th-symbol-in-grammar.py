class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        #mad
        def mad(n, k):
            if n == 1:
                return 0
            
            output = mad(n -1, ceil(k / 2))

            if k % 2 != 0:
                return output
            if output == 1:
                return 0
            return 1
    
        return mad(n, k)