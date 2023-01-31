from collections import defaultdict

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        d = defaultdict(list)
        rows = len(matrix)
        columns = len(matrix[0])
        
        for i in range ( rows):
            for j in range(columns):
                d[i-j].append(matrix[i][j])
        for keys in d.values():
            for elements in range(len(keys)-1):
                if keys[elements] != keys[elements + 1]:
                    return False
        return True
        