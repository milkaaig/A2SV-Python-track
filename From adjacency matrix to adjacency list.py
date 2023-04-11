from collections import defaultdict

n = int(input())
grid = []

for i in range(n):
    col = list(map(int, input().split()))
    grid.append(col)

adj = defaultdict(list)

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            adj[i + 1].append(j + 1)

for k, v in adj.items():
    print(len(v), end = ' ')
    print(*v)
