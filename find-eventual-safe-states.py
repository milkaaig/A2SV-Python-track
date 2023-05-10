class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        length = len(graph)
        safe = defaultdict(bool)
        output = []

        def dfs(i):
            if i in safe:
                return safe[i]
            
            safe[i] = False
            
            for neighbor  in graph[i]:
                if not dfs(neighbor):
                    return safe[i]
            
            safe[i] = True
            
            return safe[i]
        
        for i in range(length):
            if dfs(i):
                output.append(i)
        
        return output