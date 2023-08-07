from typing import List
from collections import deque
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		   
	
		seen = set()
	    
		
		def checker(i, pre):
    	    seen.add(i)
    	    
    	    for node in adj[i]:
    	        if node in seen and node != pre:
    	            return 1
    	        else:
    	            if node not in seen:
    	                if checker(node, i):
    	                    return 1
    	                
    	    return 0
		
		for i in range(V):
		    if  i not in seen:
		       
		        if checker(i, -1):
		            return 1
		return 0
		
	
		    
		    
		    
		    
		    
		
		 
		 


#{ 
 # Driver Code Starts

if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends