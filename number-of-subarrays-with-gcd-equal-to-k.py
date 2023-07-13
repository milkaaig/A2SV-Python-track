import math
class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        n = len(nums)
        output = 0
        for i in range(n):
            sub = nums[i]
            for j in range(i, n):
                sub = math.gcd(sub, nums[j])
                if sub == k:
                    output += 1
                #the gcd of multiple numbers will be decreasing or staying the same so if it's lower it ain't going higher
                elif sub < k:
                    break

                
        return output