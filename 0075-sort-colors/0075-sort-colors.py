from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = Counter(nums)
        a = dict(n)
    
       

        loc = 0
        
        if 0 in n:
            len0 = a[0]
            for i in range(len0):
                nums[i] = 0
                loc += 1
                
        if 1 in n:
            len1 = a[1]
            for i in range(len1):
                nums[loc] = 1
                loc += 1
        if 2 in n:
            len2 = a[2]   
            for i in range(len2):
                nums[loc] = 2
                loc += 1
            
        return nums
    


        
        