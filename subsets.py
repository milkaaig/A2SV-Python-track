class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        length = 2 ** len(nums)
        output = []
        
        for i  in range(length):
            a = str(bin(i))
            a = a[2:]

            if len(a) < len(nums):
                diff = len(nums) - len(a)
                a = str(0 ) * diff + a
            sub = []
           

            for j in range(len(a)):
                if a[j] == '1':
                    sub.append(nums[j])
            

            output.append(sub)
        
        return output