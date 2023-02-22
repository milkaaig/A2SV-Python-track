class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lefts = 0
        rights = 0
        length = len(nums)
        r = length -1
        l = 0
        
        
        while l <= r :
            lefts = sum(nums[0 : l])
            rights = sum(nums[l + 1 : ])
            # print("lefts" , lefts)
            # print("rights" , rights)
            if lefts == rights:
                return l
            l += 1
        
        return -1
            