class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = sqrt(c)
        r = int(r)
        l = 0
        print(r)

        while l <= r:
            two = r**2 + l**2
            
            if two == c:
                return True
            elif two  > c:
                r -= 1
            else:
                l -= 1
                
        return False
        
        