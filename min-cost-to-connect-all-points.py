class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
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
            
                
        
        cost = []

        for i in range(n):
            for j in range( n):
                if i == j:
                    continue

                dist = abs( points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                cost.append((dist, i, j))
        
        cost.sort()
        output = 0

        for dist, i, j in cost:
            if find(i) != find(j):
                output += dist
                union(i, j)  
        
        return output