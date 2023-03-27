class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        count = 0

        def mergesort(l, r, arr):
            if l == r:
                return [arr[l]]
            mid = (l + r )// 2

            left = mergesort(l, mid, arr)
            right = mergesort(mid + 1, r, arr)

            return merge(left , right)
        
        def merge(a , b):
            nonlocal count 
            j = 0

            for i in a :
                while j < len(b) and i - diff > b[j]:
                    j += 1

                count += len(b) - j

            pa , pb = 0 , 0

            res = []
            while pa<len(a) and pb<len(b):
                if a[pa] < b[pb]:
                    res.append(a[pa])
                    pa += 1
                else:
                    res.append(b[pb])
                    pb += 1

            if pa < len(a):
                res.extend(a[pa:])
            if pb < len(b):
                res.extend(b[pb:])

            return res

        d = [ n1-n2 for n1, n2 in zip(nums1, nums2)]
        mergesort(0,len(d)-1, d)

        return count