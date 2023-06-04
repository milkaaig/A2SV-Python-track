class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dic = [0] * (n  + 1)
        dic[n] = 0

        def dp(indx):
            if indx >= n:
                return 0

            if dic[indx] > 0:
                return dic[indx]

            dic[indx] = cost[indx] + min(dp(indx + 1) , dp(indx + 2))

            return dic[indx]

        dp(0)
        
        return min(dic[0], dic[1])