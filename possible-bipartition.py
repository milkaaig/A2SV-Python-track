class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        child = defaultdict(list)

        for i , j in dislikes:
            child[i].append(j)
            child[j].append(i)
        
        colored = [-1] * (n + 1)

        def checker(node, color):
            if colored[node] != -1 and colored[node] != color:
                return False

            if colored[node] == -1:
                colored[node] = color

                for i in child[node]:
                    if not checker(i, abs(1 - color)):
                        return False
            
            return True
        
        for i in range(1, n + 1):
            if colored[i] == -1:
                if not checker(i, 0):
                    return False
        
        return True