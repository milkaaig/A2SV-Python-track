class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        size = len(nums)
        output = 0
        l = 0
        r = size - 1
        print(nums[l] , nums[r])
        
        while l < r:
           
            if nums[l] + nums[r] == k:
                output += 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] > k:
                r -= 1
            elif nums[l] + nums[r] < k:
                l += 1
        
        return output
        
        