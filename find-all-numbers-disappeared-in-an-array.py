class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dict = {}
        length = len(nums)

        for i in nums:
            dict[i] = 1

        output = []

        for i in range(1, length + 1):
            if i not in dict:
                output.append(i)
        
        return output