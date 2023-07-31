class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        ans = [0] * n

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def dfs(child,parent):
            tracker = defaultdict(int)

            for node in graph[child]:
                if node != parent:
                    childnode = dfs(node, child)
                    for i, j in childnode.items():
                        tracker[i] += j
            

            tracker[labels[child]] += 1
            ans[child] = tracker[labels[child]]

            return tracker

        dfs(0, 0)
        return ans