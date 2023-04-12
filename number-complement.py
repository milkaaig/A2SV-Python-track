class Solution:
    def findComplement(self, num: int) -> int:

        shift = 1

        while shift  <= num:
            num = num ^ shift
            shift = shift << 1
        
        return num