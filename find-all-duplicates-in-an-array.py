class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dict = {}
        output = []

        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                output.append(i)
        
        return output