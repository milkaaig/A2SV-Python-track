class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        prime = set()

        for i in nums:
            p = 2

            while p * p <= i:
                while i % p == 0:
                    i //= p
                    prime.add(p)

                p += 1

            if i > 1:
                prime.add(i)

        return len(prime)