from typing import List
from collections import defaultdict
from collections import deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        graph = defaultdict(list)
        incoming = {}
        que = deque()
        output = [0] * (n + 1)
        
        for u,v in edges:
            graph[u].append(v)
            
            if v in incoming:
                incoming[v] += 1
            else:
                incoming[v] = 1
        
        for i in range(1, n + 1):
            if i not in incoming:
                que.append(i)
        
        
        time = 0
        
        while que:
        
            length = len(que)
            
            time += 1
            
            for _ in range(length):
                vert = que.popleft()
                
                for node in graph[vert]:
                    incoming[node] -= 1
                    
                    if incoming[node] == 0:
                        que.append(node)
                    
                        
                output[vert] = time
        
            
        
        output.pop(0)
        
        return output
        
            
        # code here
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends