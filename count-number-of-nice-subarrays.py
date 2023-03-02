class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        size = len(nums)
        curr = 0
        output = 0
        map = {}
        map[0] = 1

        for i in range(size):
            if nums[i] % 2 == 1:
                curr += 1
            x = map.get(curr, 0) + 1
            map[curr] = x
            y = map.get(curr - k, 0)
            output += y
        
        return output