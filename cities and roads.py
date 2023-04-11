row = int(input())
grid = []

for i in range(row):
    rowinput = list(map(int, input().split()))
    grid.append(rowinput)

roads = 0
col = row

for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 :
            roads += 1

print(roads // 2)
