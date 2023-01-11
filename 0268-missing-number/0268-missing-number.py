class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        # print(n)
        # checks if every number matches it's index 
        for i in range(n):
            #if not prints the index
            if i != nums[i]:
                return i
        return (n)