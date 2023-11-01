class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)    
        n = len(matrix[0])
        r = set()
        c = set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)
        r = list(r)
        c = list(c)
        
        for row in r:
            for j in range(n):
                matrix[row][j] = 0
    
        for col in c:
            for j in range(m):
                matrix[j][col] = 0