class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        length = len(arr)
        count = 2
        Max = count

        if length == 1:
            return 1
        
        if length == 2 :
            if arr[0] == arr[1]:
                
                return 1
            else:
                return 2
        turb = set(arr)
        if len(turb ) == 1:
            return 1
            
        

        
        for i in range(1, length - 1):
            if arr[i - 1] > arr[i]  and arr[i] < arr[i + 1]:
                count += 1
            elif arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                count += 1
            else:
                count = 2
            
            Max = max(count, Max)

        return Max