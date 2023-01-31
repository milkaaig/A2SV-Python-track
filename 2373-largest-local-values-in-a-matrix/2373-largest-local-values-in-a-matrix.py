class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n  = len(grid)
        m = n - 2
        # maxlocal = [[0 for _ in range(m)] for _ in range(m)]
        maxlocal = []
        
        def checkmax(row, col):
            maxtemp = 0
            
            for i in range(3):
                for j in range(3):
                    maxtemp = max(maxtemp , grid[i + row][j + col])
                    
            return maxtemp
        
        
        for _ in range(m):
            temp = []
            for _ in range(m):
                temp.append(0)
            maxlocal.append(temp)
      
        for i in range(n - 2):
            for j in range(n - 2): 
                maxt = checkmax(i, j)
                maxlocal[i][j] = maxt
                
        return maxlocal
    