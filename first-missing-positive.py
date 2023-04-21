class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        dic = defaultdict(int)

        for i in nums:
            if i > 0:
                 dic[i] += 1

        i = 1

        while True:
            if i not in dic:
                return i
            else:
                i += 1