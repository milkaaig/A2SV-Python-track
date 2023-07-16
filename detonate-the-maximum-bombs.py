class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x1 - x2) **2 + (y1 - y2) ** 2)

                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)
        
        def dfs(i, visit):
            if i in visit:
                return 0

            visit.add(i)
            for neighbor in adj[i]:
                dfs(neighbor, visit)
            
            return len(visit)


        output = 0
        for i in range(n):
            output = max(output, dfs(i, set()))
        
        return output