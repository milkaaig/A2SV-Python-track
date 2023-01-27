class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortednum = sorted(nums)
        output = []
        for num in nums:
            output.append(sortednum.index(num))
        return output