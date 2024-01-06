class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        length = len(nums)
        minm = []
        minval = float('inf')

        for i in range(length):
            minval = min(nums[i], minval)
            minm.append(minval)
   

        stack = []

        for i in range(length):

            while stack and nums[stack[-1]] < nums[i]:
               
                stack.pop()
 
            if stack:
                I = minm[stack[-1]]#[3] cur=1 
                J = nums[i]
                K = nums[stack[-1]]
                
                
                
                if I < J < K:
                    return True
            
            stack.append(i)

           
        
        return False