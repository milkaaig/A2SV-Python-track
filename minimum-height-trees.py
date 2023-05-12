class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        degree = defaultdict(int)
        
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
            degree[i] += 1
            degree[j] += 1

        q = deque()
       
        for key ,val in degree.items(): 
            if val == 1:
                q.append(key)
              

            if val == n - 1:
                return [key]
        
        root = []
        dist = defaultdict(int)


        while q:
            l = len(q)
           
            for i in range(l):
                node = q.popleft()

                for neighbor in graph[node]:
                    degree[node] -= 1
                    degree[neighbor] -= 1

                   
                    if degree[neighbor] == 1 :
                        q.append(neighbor)
                        dist[neighbor] = max(dist[neighbor] , dist[node] + 1)
        
        maxdist = max(dist.values())

        for key, val in dist.items():
            if val == maxdist:
                root.append(key)
        
        return root