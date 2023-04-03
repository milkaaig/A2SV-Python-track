class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        length = len(nums)

        diff = 0

        for i in range(length):
           diff ^= nums[i]
        
        return diff