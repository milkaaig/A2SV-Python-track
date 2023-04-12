class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes = [0] * n
        output = []

        for i , j in edges:
            nodes[j] = 1
        
        for i in range(len(nodes)):
            if nodes[i] == 0:
                output.append(i)
        
        return output