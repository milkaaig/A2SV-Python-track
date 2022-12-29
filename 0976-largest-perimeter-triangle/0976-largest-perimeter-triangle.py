class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        leng = len(nums)
        for sides in range(leng-3,-1,-1):
            if nums[sides] + nums[sides + 1] > nums[sides + 2]:
                return nums[sides] + nums[sides + 1] + nums[sides + 2]
        return 0