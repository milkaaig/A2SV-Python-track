import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        count = 0
        n = len(matrix)
        heap = []

        for i in range(n):
            for j in range(n):
                if len(heap) < k:
                    heappush(heap, -matrix[i][j])
                else:
                    heappushpop(heap, -matrix[i][j])
        
        return -heap[0]