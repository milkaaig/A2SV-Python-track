class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        def SieveOfEratosthenes(num):
            prime = [True for i in range(num+1)]
            p = 2

            while (p * p <= num):
                if (prime[p] == True):
                    for i in range(p * p, num+1, p):
                        prime[i] = False
                p += 1
            
            return prime

        prime = SieveOfEratosthenes(n)

        if prime[n]:
            return n
        
        factors = []
        num = n
        for i in range(2, n + 1):
            while num % i == 0:
                factors.append(i)
                num = num // i
        
        return sum(factors)