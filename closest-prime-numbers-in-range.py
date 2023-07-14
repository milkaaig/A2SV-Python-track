import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        output = [-1, -1]
        prime = []
       
        def SieveOfEratosthenes(num):
            sieve = [True for i in range(num+1)]
            p = 2

            while (p * p <= num):
                if (sieve[p] == True):
                    for i in range(p * p, num+1, p):
                        sieve[i] = False

                p += 1

            return sieve
        
        sieve = SieveOfEratosthenes(right)

        for i in range(right + 1):
            if sieve[i] and i >= left:
                prime.append(i)
        
        prime = set(prime)
        
        for i in range(left, right + 1):
            if i in prime:
                for j in range(i + 1, right + 1):
                    if j in prime:
                        diff1 = output[1] - output[0]
                        diff2 = j - i
                        if diff2 == 2 or diff2 == 1:
                            if i == 1:
                                continue
                            return [i, j]
                        elif diff1 == 0:
                            output = [i, j]
                        elif diff2 < diff1:
                            output = [i, j]
                        
        
        return output