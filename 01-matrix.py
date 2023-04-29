class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        visited = set()
        row = len(mat)
        col = len(mat[0])
        output = [[0 for j in range(col) ]for i in range(row)]
        q = deque()
       

        inbound = lambda r, c: 0 <= r < row and 0 <= c < col

        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    output[i][j] = 0
                    visited.add((i, j))
                    q.append((i, j))

        while q:    
            r, c = q.popleft()
            
            for i , j in directions:
                nr = i + r
                nc = j + c

                
                if inbound(nr, nc) and (nr, nc) not in visited:
                    output[nr][nc] = output[r][c] + 1
                    visited.add((nr, nc))
                    q.append((nr, nc))
                    
        return output