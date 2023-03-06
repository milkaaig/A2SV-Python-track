class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        val = 0
        left = 0
        right =  length - 1

        while left <= right:
            mid = left +  (right - left) // 2 

            if nums[mid] > target:
                right =  mid - 1 
                
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left