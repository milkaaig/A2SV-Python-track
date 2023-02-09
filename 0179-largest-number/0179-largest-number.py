import functools
# Since cmp_to_key sorts in ascending order .It needs to be manipulated to
# work in descending order

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = map (str, nums)
        
        # The callable function built for(cmp to key) 
        def mycmp(a , b):
        #  a = b +1 interms of position
        # means a and b need to exchange
            if a + b > b + a:
                return -1
        
            elif a + b > b + a:
                return
            
        #  mean a = b            
            else:
                return 0

        # sorting them to form largest number           
        nums = sorted(nums, key = cmp_to_key(mycmp))
        
        if nums[0] == '0':
            return str(0)
        
        nums = str(''.join(nums)) 
        # nums = '"' + nums +'"'
        return nums
        