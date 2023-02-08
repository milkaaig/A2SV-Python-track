from collections import defaultdict

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        def magic_square(subgrid) -> bool:
            distinct = set()
            
            for i in range(3):
                for j in range(3):
                    distinct.add(subgrid[i][j])
          
                    
            distinct = list(distinct)
            distinct.sort()
            ot = 1
            if len(distinct) > 9 or len(distinct) < 9:
                return False
            elif len(distinct) == 9:
                for i in range(9):
                    if distinct[i ] != ot:
                        return False
                    ot += 1
            sumofr = sum(subgrid[0])
            for r in subgrid:
                if sumofr != sum(r):
                    return False
            
            sumofc = subgrid[0][0] + subgrid[1][0] + subgrid[2][0]
            c = 0
            for _ in range(3):
                sumc = subgrid[0][c] + subgrid[1][c] + subgrid[2][c]
                if sumofc != sumc:
                    return False
                c += 1
            leftdiagonal = 0
            rightdiagonal = 0
            
            for i in range(3):
                leftdiagonal += subgrid[i][i]
                rightdiagonal += subgrid[i][2 - i]
                
            if leftdiagonal != rightdiagonal:
                return False
            
            return True
                
                
            
        
        row = len(grid)
        col = len(grid[0])
        output = 0
        
        for i in range( row - 2):
            for j in range(col - 2):
                subgrid =[ grid[i][j : j + 3] , grid[i + 1][j : j + 3] , grid[i + 2][j : j + 3]]
                
                if magic_square(subgrid):
                    output += 1
                    
        return output
        
        
            
            
        
        