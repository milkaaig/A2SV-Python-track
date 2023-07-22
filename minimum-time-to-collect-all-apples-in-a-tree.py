class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        mint = 0
        seen = set()

        for i,j  in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(node, time):
            mintm = 0
            seen.add(node)

            for child in graph[node]:
                if child in seen:
                    continue
                else:
                    time = dfs(child, 0)
                    if hasApple[child] or time:
                        mintm += 2  + time 

            return mintm

        return dfs(0, 0)