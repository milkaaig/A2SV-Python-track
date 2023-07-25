class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[0, -1],[-1, 0],[1, 0],[0, 1]]
        row, col = len(grid1), len(grid1[0])
        visited = set()
        graph1 = defaultdict(list)
        graph2 = defaultdict(list)
        output = 0

        inbound = lambda r , c: (0 <= r < row) and (0 <= c < col)

        def dfs(r, c, key):
            visited.add((r, c))
            graph2[key].append((r,c))
            

            for i, j in directions:
                nr , nc = i + r, j + c

                if inbound(nr, nc) and grid2[nr][nc] == 1 and (nr, nc) not in visited:
                    dfs(nr, nc, key)


        def checker(key):
            n = len(graph2[key])
            c = 0

            for i, j in graph2[key]:
                if grid1[i][j] == grid2[i][j]:
                    c += 1
            if c == n:
                return True
            else:
                return False


        key = 0
        for i in range(row):
            for j in range(col):
                if grid2[i][j] == 1 and (i, j) not in visited:
                    key += 1
                    dfs(i, j, key)
                    if checker(key):
                        output += 1

        return output