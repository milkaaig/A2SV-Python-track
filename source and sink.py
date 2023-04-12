from collections import defaultdict

n = int(input())
grid = []

for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

source = [0] * n
sink = [0] * n

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            source[j] = 1
            sink[i] = 1

print(source.count(0), end = ' ')
prnt = []
for i in range(n):
    if source[i] == 0:
        prnt.append(i + 1)
print(*prnt)

prnt.clear()
print(sink.count(0), end = ' ')

for i in range(n):
    if sink[i] == 0:
        prnt.append(i + 1)
print(*prnt)