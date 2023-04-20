class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        output = set()

        def sub (idx, ans):

            if len(ans) >= 2:
                output.add(tuple(ans))

            if idx >= length:
                return

        
            if not ans or nums[idx] >= ans[-1]:
                sub(idx + 1, ans)
                sub(idx + 1, ans + [nums[idx]])
            else:
                sub(idx + 1, ans)

            
        sub(0, [])

        return output