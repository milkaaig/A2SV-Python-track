class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        length = len(nums)
        # maps = defaultdict(int)
        maps = {0 : 1}
        add = 0
        output = 0

        for i in range(length):
            add += nums[i]

            if add - goal in maps:
                output += maps[add - goal]
            
            if add not in maps:
                maps[add] = 1
            
            else:
                maps[add] += 1

        print (maps)

        return output