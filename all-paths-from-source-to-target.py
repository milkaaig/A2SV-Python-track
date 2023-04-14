class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph) 
        output = []
        path = [0]

        def visit(path):
            if path[-1] == n - 1:
                output.append(path[:])
                return

            # will be traversing through nodes of nodes
            for i in (graph[path[-1]]):
                # [a] + [b] = [a, b]
                visit(path + [i])

        visit(path)

        return output