class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minm = min(nums)
        maxm  = max(nums)
        output  = 1

        for i in range(1, minm + 1):
            if minm % i ==0 and maxm % i == 0:
                output = max(i, output)
                
        return output