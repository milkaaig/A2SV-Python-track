class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        shift = 1
        count = 0

        while shift <= xor:
            if shift & xor != 0:
                count += 1
            shift = shift << 1
        return count