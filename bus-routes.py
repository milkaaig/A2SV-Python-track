class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        graph = defaultdict(list)
        n = len(routes)

        for i in range(n):
            for j in range(len(routes[i])):
                #we are looking at them as bus no 1, 2, 3...
                graph[routes[i][j]].append(i)
        
        que = deque()
        seen = set()
        for bus in graph[source]:
            for stop in routes[bus]:
                que.append(stop)
            #every bus stop that bus goes around is added to the que
            seen.add(bus)

        least = 1

        while que:
            n = len(que)

            for _ in range(n):
                stop = que.popleft()

                if stop == target:
                    return least

                for bus in graph[stop]:
                    #if that bus is not seen means that it's bus stops are not checked yet
                    if bus not in seen:
                        for stops in routes[bus]:
                            que.append(stops)

                        seen.add(bus)

            least += 1
        
        return -1