from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = 9
        col = 9
        
        
        for i in range(row):
            dic = defaultdict(int)
            for j in range(col):
                if board[i][j] != '.':
                    if dic[board[i][j]] == 1:
                        return False
                    dic[board[i][j]] += 1

        
        for j in range(col):
            dic = defaultdict(int)
            for i in range(row):
                if board[i][j] != '.':
                    if dic[board[i][j]] == 1 :
                        return False
                    dic[board[i][j]] += 1
        
        dic = set()
        row = 0
        col = 0
        while row < 9:
            col =0
            
            while col < 9:

                for i in range(row,row +3):
                    for j in range(col, col+3):
                        if board[i][j] != ".":
                            if board[i][j] in dic:
                                return False
                            dic.add(board[i][j])
                
                col +=3
                dic.clear()
            
            row +=3
	

                       
        
        return True