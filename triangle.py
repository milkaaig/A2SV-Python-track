class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # memo = [[-1 for j in range(i + 1)] for i in range(n)]
        memo = {}
        
        def path(r, c):
            if r == n - 1:
                return triangle[r][c]

            if (r, c) in memo:
                return memo[(r, c)]
            
           
            lefty = path(r + 1, c)
               

            
            right = path(r + 1, c + 1)
                

            
            memo[(r,c)] = min(lefty, right) + triangle[r][c]
            return memo[(r, c)]
        
        
        return path(0, 0)