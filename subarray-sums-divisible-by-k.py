class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mab = defaultdict(int)
        output = 0
        psum = 0
        mab[0] = 1
        for i in range(len(nums)):
            psum += nums[i]
            output += mab[psum % k]
            mab[psum % k] += 1
        
        return output