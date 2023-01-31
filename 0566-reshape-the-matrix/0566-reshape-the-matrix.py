class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        output = [] 
        m = len(mat)
        n = len(mat[0])
        
        if r * c != m * n:
            return mat
        hulum = []
        
        for i in range(m):
            for j in range(n):
                hulum.append(mat[i][j]) 
                
        element = 0
        for i in range(r):
            temp = []
            for i in range(c):
                temp.append(hulum[element])
                element += 1
            output.append(temp)
        
        return output