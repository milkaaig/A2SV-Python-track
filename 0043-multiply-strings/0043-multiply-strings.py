class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        numdic = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        inum1 = 0
        inum2 = 0
        for numbers in num1:
            inum1 = 10*inum1 + numdic[numbers]
        for numbers in num2:
            inum2 = 10*inum2 + numdic[numbers]
        prod = inum1 * inum2
        return str(prod)
        
        