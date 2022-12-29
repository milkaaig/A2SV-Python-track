class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        retind = -1
        smalld = float('inf')
        leng = len(points)
        for ptr in range(leng):
            print(ptr)
            if points[ptr][0] == x or points[ptr][1] == y:
                mand = abs(x-points[ptr][0]) + abs (y -points[ptr][1])
                if mand < smalld:
                    smalld = mand
                    retind = ptr
        return retind