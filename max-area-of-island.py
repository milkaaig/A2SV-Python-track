class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row  = len(grid)

        visited = [[False for j in range(col)] for i in range(row)]
        
        def dfs(r,c):
            direction = [[-1,0], [0, -1],[0, 1],[1,0]]
            visited[r][c] = True
            per = 0

            for i ,j in direction:
                nr = i + r
                nc = j + c

                if checker(nr, nc):
                    if not visited[nr][nc]:
                        if grid[nr][nc] == 1:
                            per += 1
                            per += dfs(nr, nc)
    
                            
            
            return per

        def checker(nr, nc):
            if nr >= row or nc >= col or nr < 0 or nc < 0:
                return False

            return True

        maxm = 0

        for i  in range(row):
            for j in range(col):
                if grid[i][j] == 1 and not visited[i][j]:
                    area =  dfs(i, j) + 1
                    maxm = max(maxm, area)
        
        return maxm