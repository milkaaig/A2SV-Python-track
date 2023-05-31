class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        directions = [[0, 1], [1, 0]]
        memo =[[0 for i in range(n)]for j in range(m)]
        memo[m -1][n- 1] = 1

        inbound = lambda r, c: 0 <= r < m and 0 <= c < n


        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if inbound(i + 1, j):
                    memo[i][j] += memo[i + 1][j]
                if inbound(i, j + 1):
                    memo[i][j] += memo[i][j + 1]
        
        return memo[0][0]