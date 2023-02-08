class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        
#         If we reverse elements on the same diagonal and reverse what we reversed we get an image             rotated at 90 degrees.
            
        for i in range(row):
#             One is add to the J to match diagonals
            for j in range(1 + i, col):
                matrix[i][j] , matrix[j][i] = matrix[j][i] , matrix[i][j]
                
        for i in matrix:
            i.reverse()
        print(matrix)