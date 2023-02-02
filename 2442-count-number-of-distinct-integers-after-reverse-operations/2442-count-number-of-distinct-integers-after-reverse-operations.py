class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            if nums[i] <= 9:
                pass
            rev = str(nums[i])[::-1]
            nums.append(int(rev))

        d = set()
        distinct = 0

        for i in nums:
            if i in d:
                pass
            else:
                d.add(i)
                distinct += 1
            
        return distinct