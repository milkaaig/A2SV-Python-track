class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        directions = [[0, 1],[0, -1], [1, 0],[-1, 0]]
        org = image[sr][sc]
        
        visited = set()
        def fill(r, c):
            visited.add((r,c))
            image[r][c] = color

            for i , j in directions:
                nr = r + i
                nc = c + j

                if inbound(nr, nc):
                    if image[nr][nc] == org and (nr, nc) not in visited:
                        fill(nr, nc)
            return

        def inbound(nr, nc):
            if (0 <= nr < row ) and  (0 <= nc < col):
                return True

            return False

        fill(sr, sc)

        return image