class Solution:
    def numTrees(self, n: int) -> int:
        memo = defaultdict(int)

        def unique(n):
            if n <= 1:
                return 1

            if n == 2:
                return 2
            
            if n in memo:
                return memo[n]

            total = 0
            for i in range(1, n + 1):
                left = unique(i - 1)
                right = unique(n - i)

                total += left * right
            
            memo[n] = total
            return memo[n]
        
        return unique(n)