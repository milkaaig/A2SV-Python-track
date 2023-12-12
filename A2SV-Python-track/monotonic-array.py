class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x = sorted(nums)
        r = sorted(nums, reverse = True)
        
        if nums == x or nums == r:
            return True
        
        return False