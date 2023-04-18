class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
       
        checker = set()

        for i in nums:
            if i in checker:
                return i
            else:
                checker.add(i)