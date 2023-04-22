class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        #next time ask for assistance 
        length = len(nums)
        if length == 1 :
            return [0]
        
        output = []
        sort = []

        for i in range(length - 1, -1, -1):
            # the imaginary pos of val tells how many numbers are smaller than itself
            output.append(bisect_left(sort, nums[i]))
            sort.insert( output[-1], nums[i])
        
        return output[::-1]