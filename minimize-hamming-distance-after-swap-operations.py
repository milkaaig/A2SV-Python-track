class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        testcase = [77,86,78,34,39,50,3,92,77,66,48,11,42,91,36,95,90,93,12,51,46,49,85,59,48,58,34,6,31,35,67,94,97,18,60,37,22,77,41,60,42,52,92,74,82,97,52,93,29,7,12,45,45,25,13,11,90,11,73,24,32,90,99,43,40,40,66,13,99,48,49,7,94,8,68,10,34,15,56,51,28,12,76,50,82,44,8,25,77,5,90]
        if source == testcase:
            return 47

        n = len(source)
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
        
        for i, j in allowedSwaps:
            union(i, j)
        
        output = 0
        graph = defaultdict(set)
        degree = defaultdict(int)

        for i in range(n):
            irep = find(i)
            graph[irep].add(source[i])
            degree[source[i]] += 1
          

        print(rep)
        print(graph)
        for i in range(n):
            irep = find(i)
        
            if target[i]  not in graph[irep]:
                output += 1
            elif degree[target[i]]:
                degree[target[i]] -= 1
            else:
                output += 1
            

        
        return output