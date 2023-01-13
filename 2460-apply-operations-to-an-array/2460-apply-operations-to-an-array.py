class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = []
        countzero = 0
        for i in range(size):
            if i+1 < size:
                if nums[i+1] == nums[i]:
                    nums[i] = 2*nums[i+1]
                    nums[i+1] = 0
        for i in range(size):
            if nums[i] != 0:
                result.append(nums[i])
            else:
                countzero +=1
        for i in range(countzero):
            result.append(0)
        return result
                