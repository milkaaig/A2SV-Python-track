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
            
#         def max_subarray_sum(arr, k):
#          window_sum = sum(arr[:k])
#          max_sum = window_sum

#          for end in range(k, len(arr)):
#          window_sum += arr[end]
#          window_sum -= arr[end-k]
#          max_sum = max(max_sum, window_sum)

        return maxav