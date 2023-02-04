class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums)
        expected = sorted(set(nums))
        k = len(expected)
        
        for i in range(k):
            nums[i] = expected[i]
            
        return k