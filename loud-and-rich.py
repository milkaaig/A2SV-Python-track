class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        degree = defaultdict(int)
        graph = defaultdict(list)
        n = len(quiet)
        for i, j in richer:
            graph[i].append(j)
            degree[j] += 1

        q = deque()
       
       
        for i in range(n):
            if degree[i] == 0:
                q.append(i)

        answer = [set() for i in range(n)]

        while q:
            temp = q.popleft()

            for node in graph[temp]:
                
                answer[node].add(temp)
                answer[node].update(answer[temp])

                degree[node] -= 1
                if degree[node] == 0 :
                    q.append(node)

        output = [i for i in range(n)]
        

        for i in range(n):
            val = [(quiet[i], i)]

            if answer[i]:
                for num in answer[i]:
                    val.append((quiet[num], num))

            minm = min(val)
            output[i] = minm[1]

        
        return output