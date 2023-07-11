class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * (n + 1)
        if n >= 1:
            
            nums[1] = 1
            i = 1

            while i <= n:
                if 2 * i <= n:
                    nums[2 * i] = nums[i]
                if 2 * i + 1 <= n:
                    nums[2 * i + 1] = nums[i] + nums[i + 1]
                i += 1
        
        return max(nums)