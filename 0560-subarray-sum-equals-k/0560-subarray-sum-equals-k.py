class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        winsum = 0
        count = 0
        size = len(nums)
        
        mab = {0 : 1}
        
        for i in range(size):
            winsum += nums[i]
            
            if winsum - k in mab:
                count +=  mab[winsum - k]
                
            if winsum in mab:
                mab[winsum] += 1
            else:
                mab[winsum] = 1
             
        return count
