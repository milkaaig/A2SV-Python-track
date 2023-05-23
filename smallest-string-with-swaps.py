class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        rep = {}
        size = {}
       
        def find(x):
            if x not in rep:
                rep[x] = x
                size[x] = 1


            if rep[x] == x:
                return x
            
            root = find(rep[x])
            rep[x] = root
            
            return root

        def union(x, y):
            xrep = find(x)
            
            yrep = find(y)

            if xrep == yrep:
                return
            
          
            if size[xrep] > size[yrep]:
                rep[yrep] = xrep
                size[xrep] += size[yrep]

            else:
                rep[xrep] = yrep
                size[yrep] += size[xrep]
        
        for i, j in pairs:
            union(i, j)

        graph = defaultdict(list)
        output = 0

        for i in range(n):
            irep =  find(i)
            graph[irep].append(s[i])
        
        for key, val in graph.items():
            val.sort(reverse = True)
        
        output = ''
        for i in range(n):
            irep =  find(i)
            output += graph[irep].pop()
        
        return output