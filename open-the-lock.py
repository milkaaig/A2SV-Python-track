class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        dead = set(deadends)
        visited = set()
        visited.add("0000")
        q = deque()
        q.append([0, 0, 0, 0])
        turn = 0

        if "0000" in dead:
            return -1

        def string(temp):
            return ''.join(list(map(str, temp)))
        
        def gen(lock):
            res = []
            arr = [-1, 1]
 
            for i in range(4):
                for j in arr:
                    copy = lock[:]
                    if copy[i] == 0 and j == -1:
                        copy[i] = 9
                    elif copy[i] == 9 and j == 1:
                        copy[i] == 0
                    else:
                        copy[i] += j
                        print(copy)
               
                    res.append(copy)
                    # print(copy)

            return res
        
        while q:
            n = len(q)

            for i in range(n):
                lock = q.popleft()
                if string(lock) == target:
                    return turn
                
                child = gen(lock)
               
                for elem in child:
                    if string(elem) not in dead and string(elem) not in visited:
                        q.append(elem)
                        visited.add(string(elem))
            turn += 1

        return -1