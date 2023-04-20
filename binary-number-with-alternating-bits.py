class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        #thank kibrom
        if n % 2 == 0:
            flag = False
        else:
            flag = True
    
        while  n:
            if n & 1 == 0 and  not flag:
                flag = True

            elif n & 1 and   flag:
                flag = False

            else:
                return False
                
            n = n >> 1

        return True