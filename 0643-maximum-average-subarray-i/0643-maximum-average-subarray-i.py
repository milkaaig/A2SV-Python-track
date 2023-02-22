class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        subsum = sum(nums [ : k])
        subav = subsum / k
        maxav = subav 
        i = k
    
        
        while i  < len(nums):
            
            subsum += nums[i]
            subsum -= nums[i - k]
            subav = subsum  / k
            maxav = max(maxav , subav)
            i +=  1
            


        return maxav