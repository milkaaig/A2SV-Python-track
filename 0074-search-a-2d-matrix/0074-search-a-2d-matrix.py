class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        search = 0
        output = False
        row = len(matrix)
        col = len(matrix[0])
        
        for i in range(row):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                search = i
                print(search)
                break
                
        for j in range(col):
            print(matrix[search][j])
            if matrix[search][j] == target:
                output = True
                return output
        
        return output
                 