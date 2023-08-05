class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        ancestor = defaultdict(set)

        for u, v in edges:
            graph[u].append(v)
            incoming[v] += 1
        
        que = deque()
        
        for key in range(n):
            if not incoming[key]:
                que.append(key)
        
        while que:
            ances = que.pop()
           
            for child in graph[ances]:
                ancestor[child].update(ancestor[ances])
                ancestor[child].add(ances)
                
                incoming[child] -= 1
                if incoming[child] == 0:
                    que.append(child)

            
        
        output = [] 

        for node in range(n):
            
            output.append(sorted(list(ancestor[node])))
            

        return output