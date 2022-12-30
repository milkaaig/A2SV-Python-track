class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sizen = len(nums)
        numsarr = []
        count = 0

        for num in range(sizen):
            if nums[num] == 0:
                count += 1
            else:
                numsarr += [nums[num]]
      
        for counter in range(count):
            numsarr += [0]
        
        for num in range (sizen):
            nums[num] = numsarr[num]
            
            