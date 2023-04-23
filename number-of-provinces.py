class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()

        def countprov(visited, city):
            visited.add(city)

            for j in range(len(isConnected[city])):
                if j != city and j not in visited and isConnected[city][j] == 1:
                    countprov(visited, j)
        
        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                countprov(visited, i)
                provinces += 1
        
        return provinces