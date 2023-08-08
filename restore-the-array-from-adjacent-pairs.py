class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        seen = set()
        graph = defaultdict(list)
        output = []

        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        
        que = deque()

        for n, adj in graph.items():
            if len(adj) == 1:
                que.append(n)
                break

        while que:
            node = que.pop()
            seen.add(node)
            output.append(node)

            for adj in graph[node]:
                if adj not in seen:
                    que.append(adj)
        
        return output