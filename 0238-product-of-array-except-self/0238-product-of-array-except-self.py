class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        size = len(nums)
        prefix = [1]
        
         
        for i in range(1, size):
            prefix.append(prefix[-1] * nums[i - 1])
            
        right = nums[size - 1]
        for i in range(size - 2, -1, -1):
            prefix[i] = prefix[i] * right
            right *= nums[i]
            
        return prefix
         
          
          