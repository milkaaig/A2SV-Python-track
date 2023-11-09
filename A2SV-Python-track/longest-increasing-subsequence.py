
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        output = [inf]

        for num in nums:
            i = bisect_left(output, num)

            if i == len(output):
                output.append(num)
            output[i] = num
        
        return len(output)


