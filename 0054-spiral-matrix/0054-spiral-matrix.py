class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix) 
        col = len(matrix[0])
        r = 0
        c = 0
        lr = row - 1
        lc = col - 1
        output = []
        
        if row == 1:
            for i in range(col):
                output.append(matrix[0][i])
            return output
        
        if col == 1:
            for i in range(row):
                output.append(matrix[i][0])
            return output
        
        while   r <= lr and c < col:
            for i in range(c, lc + 1):
                if len(output) == row*col:
                    break
                output.append(matrix[r][i])
            r += 1
            print(output)
            for i in range(r, lr + 1 ):
                if len(output) == row*col:
                    break
                output.append(matrix[i][lc])
            lc -= 1
            print(output)
            for i in range(lc, c - 1 , -1):
                if len(output) == row*col:
                    break
                output.append(matrix[lr][i])
            lr -= 1
            print(output)
            for i in range(lr, r - 1, -1):
                if len(output) == row*col:
                    break
                output.append(matrix[i][c])
            c += 1
            print(output)
          
        
        if len(output) != col * row:
            if r >= lr:
                
                for i in range(c, lc + 1):
                    output.append(matrix[lr][i])
                print(output)
            else:
              
                for i in range(r, lr + 1):
                    output.append(matrix[i][lc])
                print(output)
        return output
            
            
            
                