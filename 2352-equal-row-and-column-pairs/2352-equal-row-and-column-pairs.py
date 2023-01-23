class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr =[]
        for i in range(n):
            a = []
            for j in range(n):
                a.append(grid[j][i])
               
            arr.append(a)
            
       
        count = 0
        for row in range(n):
                for col in range(n):
                    if grid[row] == arr[col]:
                        count += 1
        return count
        