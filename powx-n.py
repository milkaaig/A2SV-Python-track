class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n ==  1:
            return x
        
        if n < 0:
            n = -1 * n
            return 1 / self.myPow(x, n)
        
        if n % 2 == 0:
            
            one = int(n / 2)
            call = self.myPow(x, one)
            
            return call * call
        
        else:
            one = int(n / 2)
            two = n - one
            call1 = self.myPow(x, one)
            call2 = self.myPow(x, two )
            
            return   call1 * call2