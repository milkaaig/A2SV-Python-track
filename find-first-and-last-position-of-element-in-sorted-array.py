class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1, -1]

        n = len(nums)

        def binary_search(isleft, n):
            best = 0
            if isleft:
                best = n - 1
            left = 0
            right = n - 1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:

                    if isleft:
                        best = min(best , mid)
                        right = mid - 1
                    else:
                        best = max(best , mid)
                        left = mid + 1
                        
                elif nums[mid] < target:
                    left = mid + 1     

                else:
                    right = mid - 1

            return best

        start = binary_search(True, n)
        end = binary_search(False, n)

        if nums[start] == target and nums[end] == target:
            return [start, end]

        return [-1, -1]