class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m-1
        ptr2  =n-1
        ref=len(nums1)-1
    
        while ptr1 >=0 and ptr2 >=0:
            if nums2[ptr2] >= nums1[ptr1]:
                nums1[ref] = nums2[ptr2]
                ptr2 -= 1
                ref -= 1
            else :
                nums1[ref]=nums1[ptr1]
                ptr1 -= 1
                ref -= 1
        if ptr1 == -1 and ptr2 > -1:
            nums1[:ptr2+1]=nums2[:ptr2+1]
    


