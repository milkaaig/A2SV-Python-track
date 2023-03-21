class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxm = max(piles)
        minm = 0
        minh = len(piles)
        ans = maxm
        length = len(piles)

        while minm + 1 < maxm:
            av = (minm + maxm) // 2
            
            count = 0

            for  i in range(length):
                count += ceil(piles[i] / av)

            minh = count

            if minh <= h:
                maxm = av
            
            elif minh > h:
                minm = av

            
        return maxm