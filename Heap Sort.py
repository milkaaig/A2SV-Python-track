#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
        
    def heappop(self, heap):
        if not heap:
            return None
        min_value = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        current = 0
        self. heapify_down(heap,len(heap),current)
        return min_value
    
    def heapify_down(self, arr, n, current):
    	#write your code
        left = (2 * current) + 1
        right = (2 * current) + 2
        small = current
    
        if left < n and arr[left] < arr[small]:
            small = left
        if right < n and arr[right] < arr[small]:
            small = right
    
        if small != current:
            arr[current] , arr[small] = arr[small], arr[current]
            self.heapify_down
            
    def heappush(self, heap,value):
        heap.append(value)
        current = len(heap) - 1
        self.heapify_up(heap,current)

    def heapify_up(self, heap,current):
    	#write your code
        if  current > 0:
            parent = (current - 1) // 2
            if heap[current] < heap[parent]:
                heap[current] , heap[parent] = heap[parent], heap[current]
            self.heapify_up( heap, parent)

    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        heap = []
        for i in range(n):
            self.heappush(heap, arr[i])
            
        return heap
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        
        heap = self.buildHeap(arr, n)
        for i in range(n):
            arr[i] = self.heappop(heap)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends