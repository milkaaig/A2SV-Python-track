class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        row = len(maze)
        col = len(maze[0])
        q = deque()
        q.append((entrance[0], entrance[1]))
        wall = set()
        visited = set()
        visited.add((entrance[0], entrance[1]))
        output = 0

        inbound = lambda r, c : 0 <= r < row and 0 <= c < col

        exsit = lambda r, c : r == 0 or r == row - 1 or c == 0 or c == col - 1
        


        while q:
            n = len(q)
            

            for _ in range(n):
                r, c = q.popleft()
                

                if exsit(r, c) and [r, c] != entrance:
                    return output

                for i , j in directions:
                    nr = r + i
                    nc = c + j

                    if inbound(nr, nc) and maze[nr][nc] == "." and (nr, nc) not in visited:
                        
                        q.append((nr, nc))
                        visited.add((nr, nc))

            output += 1

        return -1