class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        d = [n1 - n2 for n1, n2 in zip(nums1, nums2) ]

        sort = []
        count = 0

        for i in d:
            count += bisect_right(sort, i + diff)
            insort(sort, i)
        
        return count