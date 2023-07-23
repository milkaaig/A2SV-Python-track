class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sor = sorted(nums)
        dic = defaultdict(int)
        n = len(nums)

        for i in range(n):
            dic[nums[i]] = i

        check = set(nums)
        count = 0
        l = 0
        r = n - 1
        print(dic)
        while l != r:
            if nums[l] > ( 2 * nums[r]) :
                count += 1
                
                r -= 1
            else:
                l += 1
                r = n - 1
        
        return count