class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        diff = defaultdict(int)
        output = []

        for i in range(length):
            
            if nums[i] in diff and nums[i] + nums[diff[nums[i]]] == target:
               
                output.append(i)
                output.append(diff[nums[i]])
                return output

            diff[target - nums[i]] += i


