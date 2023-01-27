class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        output = []
    
        size = len(nums)
        
        for i in range(size):
            if nums[i] == target:
                output.append(i)
        return output