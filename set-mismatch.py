class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        output = []
        length = len(nums)
        dic = defaultdict(int)

        for i in nums:
            dic[i] += 1
            if dic[i] == 2:
                output.append(i)

        for i in range(1, length + 1):
            if i not in nums:
                output.append(i)
                return output