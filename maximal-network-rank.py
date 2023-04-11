class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        network = defaultdict(set)

        for i , j in roads:
            network[i].add(j)
            network[j].add(i)

        degree = defaultdict(int)

        for i in range(n):
            degree[i] = len(network[i])
        
        maxnet = 0

        for i in range(n):
            x =  degree[i]

            for j in range(i + 1, n):
                y = degree[j]
        
                if j not in network[i] and  i not in network[j]:
                    maxnet = max(x + y, maxnet)
                else:
                    maxnet = max((x + y) - 1, maxnet)
        
        return maxnet