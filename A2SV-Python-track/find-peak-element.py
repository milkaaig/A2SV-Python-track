class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
       
        if length == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return length - 1
        
        l = 1
        r = length - 2
        
        while l <= r:
            mid = l + (r - l) // 2
        
            if nums[mid] < nums[mid - 1]:
                r = mid -1
            elif nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                return mid
                
        return None
    
    
