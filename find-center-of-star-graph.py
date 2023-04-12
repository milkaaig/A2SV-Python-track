class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
       
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
           
        n = len(graph.keys())

        for key, val in graph.items():
            if len(val) == n - 1:
                return key