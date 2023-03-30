class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        xor = length
        
        for i in range(length):
            xor ^= nums[i] ^ i

        return xor