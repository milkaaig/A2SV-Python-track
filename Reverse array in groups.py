#User function template for Python

class Solution:    
    #Function to reverse every sub-array group of size k.
    def reverseInGroups(self, arr, N, K):
        #the list that will be containing the reversed subarrays
        temp=[]
        #initialize our pointer
		i = 0
		#our pointer should always be less than size because indexing begins from 0
        while i < N:
            #the subarray with size k or less gets assigned to part
            part = arr[i:i+K]
            part.reverse()
            # the reversed subbarray will be stored on our temporary container
            temp += part
            # our pointer is increased by K to iterate through the next subbarray
            i += K
            # the temporary container replaces every element of arr 
        for i in range(N):
            arr[i] = temp[i]

#{ 
 # Driver Code Starts
#Initial template for Python

import math
def main():
    T=int(input())
    while(T>0):
        nk=[int(x) for x in input().strip().split()]
        N=nk[0]
        K=nk[1]
        arr=[int(x) for x in input().strip().split()]
        
        ob = Solution()
        ob.reverseInGroups(arr,N,K)
        for i in arr:
            print(i,end=" ")
        print()
        T-=1

if __name__=="__main__":
    main()




# } Driver Code Ends
