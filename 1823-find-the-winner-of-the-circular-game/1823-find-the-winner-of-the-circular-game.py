class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        num = []
        
        for i in range(n):
            num.append(i + 1)
        
        l = len(num)
        i = 0
        while len(num) > 1:
            i = (i + k - 1)%len(num)
            print(i)
            num.pop(i)
       
            
        return num[0]