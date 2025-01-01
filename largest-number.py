class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if max(nums) == 0:
            return '0'
        if len(nums) < 2:
            return str(nums[0])
        
        def choose(a, b):
            return int(a + b) > int(b + a)
        
        nums = list(map(str, nums))
        n = len(nums)

        for i in range(n):
            r = i
            l = r + 1

            while l < n:
                if choose(nums[r], nums[l]):
                    pass
                else:
                    nums[r], nums[l] = nums[l], nums[r]
                l += 1
        return "".join(nums)
        
