from collections import defaultdict

nodes = int(input())
op = int(input())
graph = defaultdict(list)

for i in range(op):
    com = list(map(int, input().split()))
    if com[0] == 1:
        graph[com[1]].append(com[2])
        graph[com[2]].append(com[1])

    else:
        print(*graph[com[1]])
