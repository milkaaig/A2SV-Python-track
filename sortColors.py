class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        dic = {0: 0, 1: 0, 2: 0}
        n = len(nums)
        c = 0

        for i in range(n):
            dic[nums[i]] += 1
        
        for i in range(dic[0]):
            nums[c] = 0
            c += 1
        
        for i in range(dic[1]):
            nums[c] = 1
            c += 1
        
        for i in range(dic[2]):
            nums[c] =2
            c += 1
