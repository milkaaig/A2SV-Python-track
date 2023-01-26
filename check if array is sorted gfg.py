#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        count = 0
        for i in range(n - 1):
            if arr[i +1] >= arr[i]:
                count += 1
        if count == n -1:
            return True
        else:
            return False
        
