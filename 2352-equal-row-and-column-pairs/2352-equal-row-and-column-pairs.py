class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        arr =[]
        for i in range(n):
            a = []
            for j in range(n):
                a.append(grid[j][i])
                # print(a)
            arr.append(a)
            
        # print(arr)
        count = 0
        for row in range(n):
                for col in range(n):
                    if grid[row] == arr[col]:
                        count += 1
        return count
        # N=len(grid)
        # arr=[]
        # for ii in range(N):
        #     a=[]
        #     for i in range(len(grid)):
        #         for j in range(len(grid[i])):
        #             if j==ii:
        #                 a.append(grid[i][j])
        #                 print(a)
        #     arr.append(a)
        #     a=[]
            # print(arr)
        # count=0
        # for xx in range(len(grid)):
        #     for yy in range(len(arr)):
        #         if grid[xx]==arr[yy]:
        #             count+=1
        # return count