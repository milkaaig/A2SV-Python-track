class Solution(object):
    def findLength(self, A, B):
        maxLen = 0
        lenA = len(A)
        lenB = len(B)
        dp = [[0]* (lenB + 1) for _ in range(lenA + 1)]
        
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i -1][j - 1] + 1
                    maxLen = max(dp[i][j], maxLen)
                
        return maxLen
        
        
   