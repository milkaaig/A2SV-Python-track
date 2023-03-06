# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        mid = left + (right - left)//2
        output = 1

        if n == 1:
            return 1

        while left <= right:
            mid = left + (right - left)//2

            if isBadVersion(mid):
                output = mid
                right =  mid - 1

            else:
                left = mid + 1
        
        return output