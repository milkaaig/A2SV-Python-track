class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        row = len(mat)

        for i in range(row):
            ans += mat[i][i]
            ans += mat[row -1 - i][i]

        if row % 2 != 0:
            ans -= mat[row // 2][row // 2]
        
        return ans
        