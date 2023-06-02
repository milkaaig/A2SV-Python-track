class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 1:
            return nums[0]
        

        def dp(indx, arr):
            if indx >= len(arr):
                return 0
            
            if indx in memo:
                return memo[indx]

            
            memo[indx] = max(dp(indx + 2, arr) + arr[indx], dp(indx + 1, arr))
            
            return memo[indx]
        
        
        first = dp(0, nums[:-1])
        memo = {}
        second = dp(0, nums[1:])
        

        return max(first, second)