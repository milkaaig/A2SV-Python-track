class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[0, -1],[-1, 0],[1, 0],[0, 1]]
        nflip = set()
        row = len(board)
        col = len(board[0])

        inbound = lambda r , c: (0 <= r < row) and (0 <= c < col)
        
        border = lambda r, c: r == 0 or r == row - 1 or c == 0 or c == col - 1
       

        def flip(i, j):
            nflip.add((i, j))
            for r, c in directions:
                nr = r + i
                nc = c + j
                if inbound(nr, nc) :
                    if board[nr][nc] == 'O' and (nr, nc) not in nflip:
                        flip(nr, nc)
                        
                
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in nflip:
                    if border(i, j) :
                        nflip.add((i,j))
                        flip(i, j)
        
        
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O" and (i, j) not in nflip:
                    board[i][j] = 'X'