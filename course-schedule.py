class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = defaultdict(int)

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0: 
                q.append(course)
        
        ordered = []

        while q:
            cur = q.popleft()
            ordered.append(cur)

            for neighbor in graph[cur]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        print(ordered)
        if len(ordered) != numCourses:
            return False

        return True