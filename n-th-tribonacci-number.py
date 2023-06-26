class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0] * 38
        f[0] = 0
        f[1] = f[2] = 1

        for i in range(38):
            if i + 3 < 38:
                f[i + 3] = f[i] + f[i + 1] + f[i + 2]
        
        return f[n]