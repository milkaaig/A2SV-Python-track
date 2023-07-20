class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)
        memo[0] = 1
        for i in range(1, target + 1):
            for j in nums:
                if j <= i:
                    memo[i] += memo[i - j]
        
        return memo[target]