class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x 

        while left <= right:
            mid = left + (right - left) // 2

            if mid * mid < x:
                output = mid
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                output = mid
                break

        return output