class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        output = []

        def perm(idx):
            if idx >= len(nums):
                output.append(nums.copy())
                return

            for i in range(idx,len(nums)):
                nums[idx],nums[i]=nums[i],nums[idx]
                perm(idx+1)
                nums[idx],nums[i]=nums[i],nums[idx]
        
    
        perm(0)
        return output