class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        n = len(arr)
        m = 0
        for i in range(n - 1):
           
            if arr[i] < arr[i + 1]:
                continue
            elif arr[i] == arr[i + 1]:
                return False
            else:
                m = i
                break
            return False
        if m != 0:
            for i in range(m, n-1):
                if arr[i] > arr[i + 1]:
                    continue
                else: 
                    return False
        else: 
            return False
        return True
    
        
            
        
