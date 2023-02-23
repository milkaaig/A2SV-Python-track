class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        psum = 0
        output = float('inf')
        start = 0
        end = 0
        count = 0
        
        while end < len(nums):
            psum += nums[end]
           
            
            while psum >= target:
                output = min((end - start ) + 1, output)
                psum -= nums[start]
                start += 1
                
            
            end += 1
            
        if output == float('inf'):
            return 0
            
        return output