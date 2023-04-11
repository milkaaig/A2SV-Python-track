class Solution(object):
    def singleNumber(self, nums):

        output = 0
        length = len(nums)
        


        for i in range(32):
            count = 0
            for n in nums:
                if n & (1 << i) > 0:
                    count += 1

            if count % 3 != 0:
                output += 2**i

        if output >= (1 << 31):
            output = output - (1<< 32)

        return output