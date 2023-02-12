class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
       
        
        for i in range(k):
            left = len(nums) - 1
            temp = nums[left]
            # print(temp)
            # print('left',left)
            nums.pop(left)
            nums.insert(0 , temp)
            
        