class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        size = len(piles)
        maxout = 0
        turn = size / 3
        count = 0
        piles.sort()
        
        for i in range(size -2,-1, -2):
            maxout += piles[i]
            count += 1
            if count == turn:
                break
        return maxout