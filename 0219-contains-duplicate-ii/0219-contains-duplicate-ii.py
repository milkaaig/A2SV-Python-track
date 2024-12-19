class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        checker = {}
        
        for i in range(n):
            if nums[i] in checker:
                if i - checker[nums[i]] <= k:
                    return True
                else:
                    checker[nums[i]] = i
            else:
                checker[nums[i]] = i
        
        return False