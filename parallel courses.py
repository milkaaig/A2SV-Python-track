from Collections import deque
def parallelCourses(n, prerequisites):
    # Write your code 
    graph = defaultdict(list)
    indegree = [0] * (n) 

    visited = set()

    for i, j in prerequisites:
        graph[i].append(j)
        indegree[j] += 1
    
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            queue.append(i)
            visited.add(i)
    
    output = 0
    while q:
        N = len(q)
        
        for i in range(N):
            node = q.popleft()

            for child in graph[node]:
                if chile not in visited:
                    indegree[child] -= 1
                    if incoming[child] == 0:
                        q.append(child)
                        visited.add(child)
        output += 1

    if len(visited) == n:
        return output

    return -1
