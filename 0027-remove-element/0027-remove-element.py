class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lngnum = len(nums)
        num = 0
        while num < lngnum:
            if nums[num] == val:
                nums.remove(val)
                lngnum -= 1
            else:
                num += 1
                
        