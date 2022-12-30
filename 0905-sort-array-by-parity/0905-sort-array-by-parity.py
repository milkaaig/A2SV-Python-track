class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        sizeofn = len(nums)
        even =[]
        count = []
        for num in range(sizeofn):
            if nums[num] %2 == 0:
                even += [nums[num]]
                
            else:
                count += [nums[num]]
        even += count
        return even